import 'dart:async';
import 'dart:convert';
import '../models/song.dart';
import '../models/playlist.dart';
import '../models/artist.dart';
import '../models/event.dart';
import '../models/song_request.dart';
import '../data/songs.dart';
import '../data/events.dart';
import '../data/playlists.dart';
import '../data/artists.dart';
import '../services/storage.dart';
import '../services/realtime.dart';

class AppState {
  String? username;
  String currentScreen = 'home';
  List<String> navigationHistory = ['home'];
  
  Event? selectedEvent = allEvents[0];
  Playlist? selectedPlaylist = allPlaylists[0];
  Song? currentSong = allSongs[0];
  
  List<SongRequest> queue = [];
  
  List<Song> likedSongs = [allSongs[0], allSongs[2], allSongs[6]];
  List<Playlist> savedPlaylists = [allPlaylists[0], allPlaylists[2]];
  List<Artist> followedArtists = [allArtists[0], allArtists[3]];
  List<Song> recentlyPlayed = [allSongs[0], allSongs[1], allSongs[2]];
  
  bool isPlaying = true;
  int currentSecondsElapsed = 72; // 1:12 elapsed
  Timer? playbackTimer;
  Timer? liveTickerTimer;

  static final AppState _instance = AppState._internal();
  factory AppState() => _instance;

  AppState._internal() {
    refreshFromStorage();
    _startPlaybackTimer();
    _startLiveTickerTimer();
  }

  void _startPlaybackTimer() {
    playbackTimer?.cancel();
    playbackTimer = Timer.periodic(const Duration(seconds: 1), (_) {
      if (isPlaying && currentSong != null) {
        currentSecondsElapsed++;
        if (currentSecondsElapsed >= currentSong!.duration) {
          nextSong();
        } else {
          notifyListeners();
        }
      }
    });
  }

  void _startLiveTickerTimer() {
    liveTickerTimer?.cancel();
    liveTickerTimer = Timer.periodic(const Duration(seconds: 4), (_) {
      if (selectedEvent != null) {
        // Dynamic simulated live attendee fluctuation (+/- 3 listeners)
        final delta = (DateTime.now().second % 7) - 3;
        selectedEvent!.listenerCount = (selectedEvent!.listenerCount + delta).clamp(100, 50000);
        notifyListeners();
      }
    });
  }

  int get currentProgressPercent {
    if (currentSong == null || currentSong!.duration == 0) return 0;
    return ((currentSecondsElapsed / currentSong!.duration) * 100).clamp(0, 100).round();
  }

  String get formattedCurrentTime {
    final mins = currentSecondsElapsed ~/ 60;
    final secs = (currentSecondsElapsed % 60).toString().padLeft(2, '0');
    return '$mins:$secs';
  }

  void togglePlayPause() {
    isPlaying = !isPlaying;
    notifyListeners();
  }

  void nextSong() {
    if (currentSong == null) return;
    final currentIndex = allSongs.indexWhere((s) => s.id == currentSong!.id);
    final nextIndex = (currentIndex + 1) % allSongs.length;
    currentSong = allSongs[nextIndex];
    currentSecondsElapsed = 0;
    isPlaying = true;
    if (!recentlyPlayed.contains(currentSong)) {
      recentlyPlayed.insert(0, currentSong!);
    }
    notifyListeners();
  }

  void prevSong() {
    if (currentSong == null) return;
    final currentIndex = allSongs.indexWhere((s) => s.id == currentSong!.id);
    final prevIndex = (currentIndex - 1 + allSongs.length) % allSongs.length;
    currentSong = allSongs[prevIndex];
    currentSecondsElapsed = 0;
    isPlaying = true;
    notifyListeners();
  }

  void refreshFromStorage() {
    final savedQueueJson = StorageService.getItem('tune_queue_data');
    if (savedQueueJson != null && savedQueueJson.isNotEmpty) {
      try {
        final List decoded = jsonDecode(savedQueueJson) as List;
        queue = decoded.map((e) => SongRequest.fromJson(Map<String, dynamic>.from(e as Map))).toList();
        queue.sort((a, b) => b.requestCount.compareTo(a.requestCount));
      } catch (e) {
        _initDefaultQueue();
      }
    } else {
      _initDefaultQueue();
    }
  }

  void _initDefaultQueue() {
    queue = [
      SongRequest(
        id: 'req1',
        song: allSongs[0],
        requesters: ['Ayaan', 'Rahul'],
        requestCount: 2,
        timestamp: '2 mins ago',
      ),
      SongRequest(
        id: 'req2',
        song: allSongs[6],
        requesters: ['Priya', 'Ananya'],
        requestCount: 2,
        timestamp: 'Just now',
      )
    ];
    _saveQueueToStorage();
  }

  void _saveQueueToStorage() {
    final encoded = jsonEncode(queue.map((r) => r.toJson()).toList());
    StorageService.setItem('tune_queue_data', encoded);
  }

  void syncQueueFromPayload(String rawJson) {
    try {
      if (rawJson.trim().isEmpty) return;
      final List decoded = jsonDecode(rawJson) as List;
      queue = decoded.map((e) => SongRequest.fromJson(Map<String, dynamic>.from(e as Map))).toList();
      queue.sort((a, b) => b.requestCount.compareTo(a.requestCount));
      _saveQueueToStorage();
      notifyListeners();
    } catch (e) {
      print('Sync queue error: $e');
    }
  }
  
  List<VoidCallback> listeners = [];
  
  void addListener(VoidCallback listener) {
    listeners.add(listener);
  }
  
  void notifyListeners() {
    for (var listener in listeners) {
      listener();
    }
  }

  void pushScreen(String screen) {
    if (currentScreen != screen) {
      navigationHistory.add(screen);
      currentScreen = screen;
      notifyListeners();
    }
  }

  void popScreen() {
    if (navigationHistory.length > 1) {
      navigationHistory.removeLast();
      currentScreen = navigationHistory.last;
      notifyListeners();
    }
  }

  bool get canGoBack => navigationHistory.length > 1;

  void openPlaylist(Playlist playlist) {
    selectedPlaylist = playlist;
    pushScreen('playlist_detail');
  }

  void upvoteRequest(SongRequest req) {
    final name = username ?? 'Vrish';
    if (req.requesters.contains(name)) {
      req.requesters.remove(name);
      req.requestCount = req.requesters.length;
    } else {
      req.requesters.add(name);
      req.requestCount = req.requesters.length;
    }
    queue.sort((a, b) => b.requestCount.compareTo(a.requestCount));
    _saveQueueToStorage();
    RealtimeService.broadcastQueue(jsonEncode(queue.map((r) => r.toJson()).toList()));
    notifyListeners();
  }

  void addRequest(Song song) {
    final name = username ?? 'Vrish';
    final existingReq = queue.where((r) => r.song.id == song.id).firstOrNull;
    if (existingReq != null) {
      if (!existingReq.requesters.contains(name)) {
        existingReq.requesters.add(name);
        existingReq.requestCount = existingReq.requesters.length;
      }
    } else {
      queue.add(SongRequest(
        id: DateTime.now().millisecondsSinceEpoch.toString(),
        song: song,
        requesters: [name],
        requestCount: 1,
        timestamp: 'Just now',
      ));
    }
    queue.sort((a, b) => b.requestCount.compareTo(a.requestCount));
    _saveQueueToStorage();
    RealtimeService.broadcastQueue(jsonEncode(queue.map((r) => r.toJson()).toList()));
    notifyListeners();
  }

  void toggleLikeSong(Song song) {
    if (likedSongs.contains(song)) {
      likedSongs.remove(song);
      song.isLiked = false;
    } else {
      likedSongs.add(song);
      song.isLiked = true;
    }
    notifyListeners();
  }

  void toggleSavePlaylist(Playlist playlist) {
    if (savedPlaylists.contains(playlist)) {
      savedPlaylists.remove(playlist);
      playlist.isSaved = false;
    } else {
      savedPlaylists.add(playlist);
      playlist.isSaved = true;
    }
    notifyListeners();
  }

  void toggleFollowArtist(Artist artist) {
    if (followedArtists.contains(artist)) {
      followedArtists.remove(artist);
      artist.isFollowing = false;
    } else {
      followedArtists.add(artist);
      artist.isFollowing = true;
    }
    notifyListeners();
  }
}

typedef VoidCallback = void Function();
