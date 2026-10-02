import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

base_dir = "/Users/vrishthadani/Desktop/TuneRequest/tunerequest/lib"

files = {
    "models/song.dart": """class Song {
  final String id;
  final String title;
  final String artist;
  final String album;
  final String genre;
  final String language;
  final int duration;
  final String coverImage;
  bool isLiked;

  Song({
    required this.id,
    required this.title,
    required this.artist,
    required this.album,
    required this.genre,
    required this.language,
    required this.duration,
    required this.coverImage,
    this.isLiked = false,
  });

  Map<String, dynamic> toJson() => {
    'id': id,
    'title': title,
    'artist': artist,
    'album': album,
    'genre': genre,
    'language': language,
    'duration': duration,
    'coverImage': coverImage,
    'isLiked': isLiked,
  };

  factory Song.fromJson(Map<String, dynamic> json) => Song(
    id: json['id'] as String,
    title: json['title'] as String,
    artist: json['artist'] as String,
    album: json['album'] as String,
    genre: json['genre'] as String,
    language: json['language'] as String,
    duration: json['duration'] as int,
    coverImage: json['coverImage'] as String,
    isLiked: json['isLiked'] as bool? ?? false,
  );

  String get formattedDuration {
    final mins = duration ~/ 60;
    final secs = (duration % 60).toString().padLeft(2, '0');
    return '$mins:$secs';
  }
}""",
    "models/artist.dart": """class Artist {
  final String id;
  final String name;
  final String imageUrl;
  final String genre;
  final int followers;
  bool isFollowing;

  Artist({
    required this.id,
    required this.name,
    required this.imageUrl,
    required this.genre,
    required this.followers,
    this.isFollowing = false,
  });
}""",
    "models/playlist.dart": """import 'song.dart';

class Playlist {
  final String id;
  final String name;
  final String description;
  final String coverImage;
  final List<Song> songs;
  bool isSaved;

  Playlist({
    required this.id,
    required this.name,
    required this.description,
    required this.coverImage,
    required this.songs,
    this.isSaved = false,
  });
}""",
    "models/song_request.dart": """import 'song.dart';

class SongRequest {
  final String id;
  final Song song;
  final List<String> requesters;
  int requestCount;
  final String timestamp;

  SongRequest({
    required this.id,
    required this.song,
    required this.requesters,
    this.requestCount = 1,
    required this.timestamp,
  });

  Map<String, dynamic> toJson() => {
    'id': id,
    'song': song.toJson(),
    'requesters': requesters,
    'requestCount': requestCount,
    'timestamp': timestamp,
  };

  factory SongRequest.fromJson(Map<String, dynamic> json) => SongRequest(
    id: json['id'] as String,
    song: Song.fromJson(Map<String, dynamic>.from(json['song'] as Map)),
    requesters: List<String>.from(json['requesters'] as List),
    requestCount: json['requestCount'] as int,
    timestamp: json['timestamp'] as String? ?? 'Just now',
  );
}""",
    "models/event.dart": """class Event {
  final String id;
  final String name;
  final String location;
  final String date;
  final String time;
  final String host;
  final int listenerCount;
  final String category;
  final String currentSongId;
  final String bannerImage;

  Event({
    required this.id,
    required this.name,
    required this.location,
    required this.date,
    required this.time,
    required this.host,
    required this.listenerCount,
    required this.category,
    required this.currentSongId,
    required this.bannerImage,
  });
}""",
    "data/songs.dart": """import '../models/song.dart';

final List<Song> allSongs = [
  Song(id: 's1', title: 'Kesariya', artist: 'Arijit Singh', album: 'Brahmastra', genre: 'Bollywood', language: 'Hindi', duration: 268, coverImage: 'https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=400&q=80'),
  Song(id: 's2', title: 'Naatu Naatu', artist: 'Rahul Sipligunj & Kaala Bhairava', album: 'RRR', genre: 'Telugu Folk', language: 'Telugu', duration: 215, coverImage: 'https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=400&q=80'),
  Song(id: 's3', title: 'Husn', artist: 'Anuv Jain', album: 'Husn Single', genre: 'Indie Acoustic', language: 'Hindi', duration: 218, coverImage: 'https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=400&q=80'),
  Song(id: 's4', title: 'Kala Chashma', artist: 'Amar Arshi, Badshah', album: 'Baar Baar Dekho', genre: 'Party Mashup', language: 'Hindi/Punjabi', duration: 187, coverImage: 'https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=400&q=80'),
  Song(id: 's5', title: 'Gali Gali', artist: 'Neha Kakkar', album: 'KGF Chapter 1', genre: 'Item Dance', language: 'Hindi', duration: 204, coverImage: 'https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=400&q=80'),
  Song(id: 's6', title: 'Illuminati', artist: 'Sushin Shyam, Dabzee', album: 'Aavesham', genre: 'South Hip-Hop', language: 'Malayalam', duration: 172, coverImage: 'https://images.unsplash.com/photo-1501386761578-eac5c94b800a?w=400&q=80'),
  Song(id: 's7', title: 'Tauba Tauba', artist: 'Karan Aujla', album: 'Bad Newz', genre: 'Punjabi Commercial', language: 'Punjabi', duration: 208, coverImage: 'https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?w=400&q=80'),
  Song(id: 's8', title: 'Zingaat', artist: 'Ajay-Atul', album: 'Sairat', genre: 'Marathi Energetic', language: 'Marathi', duration: 228, coverImage: 'https://images.unsplash.com/photo-1520523839897-bd0b52f945a0?w=400&q=80'),
  Song(id: 's9', title: 'Arabic Kuthu', artist: 'Anirudh Ravichander', album: 'Beast', genre: 'Tamil Dance', language: 'Tamil', duration: 280, coverImage: 'https://images.unsplash.com/photo-1465847899084-d164df4dedc6?w=400&q=80'),
  Song(id: 's10', title: 'Pasoori', artist: 'Ali Sethi, Shae Gill', album: 'Coke Studio 14', genre: 'Indie Fusion', language: 'Punjabi', duration: 224, coverImage: 'https://images.unsplash.com/photo-1511379938547-c1f69419868d?w=400&q=80'),
  Song(id: 's11', title: 'Choo Lo', artist: 'The Local Train', album: 'Aalas Ka Pedh', genre: 'Rock Indie', language: 'Hindi', duration: 234, coverImage: 'https://images.unsplash.com/photo-1459749411175-04bf5292ceea?w=400&q=80'),
  Song(id: 's12', title: 'Chaleya', artist: 'Arijit Singh, Shilpa Rao', album: 'Jawan', genre: 'Romantic Pop', language: 'Hindi', duration: 200, coverImage: 'https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=400&q=80')
];""",
    "data/artists.dart": """import '../models/artist.dart';

final List<Artist> allArtists = [
  Artist(id: 'a1', name: 'Arijit Singh', genre: 'Bollywood Romantic', followers: 85200000, imageUrl: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&q=80', isFollowing: true),
  Artist(id: 'a2', name: 'Anirudh Ravichander', genre: 'Tamil Pop / Rock', followers: 42100000, imageUrl: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&q=80', isFollowing: false),
  Artist(id: 'a3', name: 'Karan Aujla', genre: 'Punjabi Hip Hop', followers: 29400000, imageUrl: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&q=80', isFollowing: true),
  Artist(id: 'a4', name: 'Anuv Jain', genre: 'Indie Acoustic', followers: 18500000, imageUrl: 'https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=400&q=80', isFollowing: true),
];""",
    "data/playlists.dart": """import '../models/playlist.dart';
import 'songs.dart';

final List<Playlist> allPlaylists = [
  Playlist(
    id: 'p1',
    name: 'College Fest Bangers',
    description: 'The highest requested tracks across top campus pro-nites',
    coverImage: 'https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=400&q=80',
    songs: [allSongs[0], allSongs[1], allSongs[3], allSongs[5], allSongs[7]],
    isSaved: true,
  ),
  Playlist(
    id: 'p2',
    name: 'Navratri Garba Beats',
    description: 'High energy fusion tracks for non-stop dance',
    coverImage: 'https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=400&q=80',
    songs: [allSongs[1], allSongs[3], allSongs[7]],
    isSaved: false,
  ),
  Playlist(
    id: 'p3',
    name: 'Chill Indie Sessions',
    description: 'Acoustic vibes for late-night hostel lounge requests',
    coverImage: 'https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=400&q=80',
    songs: [allSongs[2], allSongs[9], allSongs[10]],
    isSaved: true,
  ),
];""",
    "data/events.dart": """import '../models/event.dart';

final List<Event> allEvents = [
  Event(
    id: 'e1',
    name: 'IIT Bombay Mood Indigo — ProNite Stage',
    location: 'Powai, Mumbai',
    date: 'TODAY',
    time: '20:00 - LIVE',
    host: 'DJ Chetas & DJ Arjun',
    listenerCount: 3420,
    category: 'College Fest',
    currentSongId: 's1',
    bannerImage: 'https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=600&q=80',
  ),
  Event(
    id: 'e2',
    name: 'Navi Mumbai Music Night & DJ Battle',
    location: 'Seawoods Grand Central, Navi Mumbai',
    date: 'TONIGHT',
    time: '21:00 - LIVE',
    host: 'DJ Harsh & DJ Riya',
    listenerCount: 1250,
    category: 'Arena Concert',
    currentSongId: 's4',
    bannerImage: 'https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=600&q=80',
  ),
  Event(
    id: 'e3',
    name: 'Koramangala Acoustic Rooftop Jam',
    location: '12th Main, Koramangala, Bengaluru',
    date: 'TONIGHT',
    time: '21:30 - LIVE',
    host: 'DJ Rohan Roy',
    listenerCount: 410,
    category: 'Live Cafe',
    currentSongId: 's3',
    bannerImage: 'https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=600&q=80',
  ),
  Event(
    id: 'e4',
    name: 'Mehra & Kapoor Grand Sangeet Reception',
    location: 'The Leela Palace, Udaipur',
    date: 'TONIGHT',
    time: '19:00 - LIVE',
    host: 'DJ Harshita',
    listenerCount: 380,
    category: 'Wedding Sangeet',
    currentSongId: 's4',
    bannerImage: 'https://images.unsplash.com/photo-1519741497674-611481863552?w=600&q=80',
  ),
  Event(
    id: 'e5',
    name: 'Pune Campus DJ Night — COEP Cultural Fest',
    location: 'Shivajinagar, Pune',
    date: 'TOMORROW',
    time: '19:30 - UPCOMING',
    host: 'DJ Shadow Dubai',
    listenerCount: 2100,
    category: 'College Fest',
    currentSongId: 's7',
    bannerImage: 'https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=600&q=80',
  ),
  Event(
    id: 'e6',
    name: 'Delhi University North Campus Spring Fest',
    location: 'SRCC Grounds, Delhi',
    date: 'TOMORROW',
    time: '18:00',
    host: 'DJ Spinny',
    listenerCount: 1800,
    category: 'College Fest',
    currentSongId: 's7',
    bannerImage: 'https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&q=80',
  ),
  Event(
    id: 'e7',
    name: 'Bengaluru Tech & Music Mela 2025',
    location: 'Manpho Convention Centre, Bengaluru',
    date: 'OCT 18',
    time: '17:00',
    host: 'DJ Progressive India',
    listenerCount: 4500,
    category: 'Music Festival',
    currentSongId: 's9',
    bannerImage: 'https://images.unsplash.com/photo-1501386761578-eac5c94b800a?w=600&q=80',
  ),
  Event(
    id: 'e8',
    name: 'Goa Sunsets Beach Shack Jam',
    location: 'Anjuna Beach Cliff, North Goa',
    date: 'OCT 22',
    time: '18:00',
    host: 'DJ Maya Sunset',
    listenerCount: 890,
    category: 'Beach Lounge',
    currentSongId: 's10',
    bannerImage: 'https://images.unsplash.com/photo-1520523839897-bd0b52f945a0?w=600&q=80',
  )
];""",
    "app/state.dart": """import 'dart:convert';
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
  int currentProgress = 35;

  static final AppState _instance = AppState._internal();
  factory AppState() => _instance;

  AppState._internal() {
    refreshFromStorage();
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
""",
    "services/storage.dart": """import 'package:web/web.dart' as web;

class StorageService {
  static void setItem(String key, String value) {
    web.window.localStorage.setItem(key, value);
  }
  
  static String? getItem(String key) {
    return web.window.localStorage.getItem(key);
  }

  static void saveUsername(String name) {
    setItem('username', name);
  }

  static String? getUsername() {
    return getItem('username');
  }
}
""",
    "services/realtime.dart": """import 'package:web/web.dart' as web;
import 'dart:js_interop';
import '../app/state.dart';

class RealtimeService {
  static web.BroadcastChannel? _channel;
  
  static void init(Function(String) onMessage) {
    try {
      _channel = web.BroadcastChannel('tunerequest_live_v4');
      _channel!.onmessage = ((web.MessageEvent event) {
        onMessage(event.data.toString());
      }).toJS;

      web.window.addEventListener('storage', ((web.StorageEvent event) {
        if (event.key == 'tune_queue_data') {
          AppState().refreshFromStorage();
          AppState().notifyListeners();
        }
      }).toJS);
    } catch (e) {
      print('Realtime service init error: $e');
    }
  }
  
  static void broadcastQueue(String queueJsonPayload) {
    try {
      _channel?.postMessage(queueJsonPayload.toJS);
    } catch (e) {
      print('Broadcast error: $e');
    }
  }
}
""",
    "main.dart": """import 'package:web/web.dart' as web;
import 'dart:js_interop';
import 'app/state.dart';
import 'screens/home.dart';
import 'screens/live_queue.dart';
import 'screens/events.dart';
import 'screens/library.dart';
import 'screens/search.dart';
import 'screens/playlist_detail.dart';
import 'widgets/player.dart';
import 'services/storage.dart';
import 'services/realtime.dart';
import 'data/playlists.dart';

void main() {
  final appState = AppState();
  
  appState.username = StorageService.getUsername();
  if (appState.username == null || appState.username!.trim().isEmpty) {
    appState.username = web.window.prompt('What should we call you on TuneRequest?', 'Vrish') ?? 'Vrish';
    if (appState.username!.trim().isEmpty) appState.username = 'Vrish';
    StorageService.saveUsername(appState.username!);
  }
  
  RealtimeService.init((msgPayload) {
    appState.syncQueueFromPayload(msgPayload);
  });

  initUI();
}

void initUI() {
  final appContainer = web.document.querySelector('#app') as web.HTMLDivElement;
  appContainer.innerHTML = ''''''.toJS;
  
  final topBar = web.document.createElement('div') as web.HTMLDivElement;
  topBar.className = 'top-header-bar';
  topBar.innerHTML = '''
    <div class="header-left">
      <button class="nav-btn" id="btn-back" title="Go Back">◀</button>
      <div class="logo">TuneRequest <span class="badge">LIVE</span></div>
    </div>
    <div class="header-center">
      <div class="live-event-ticker">
        🔴 LIVE STAGE: <strong>${AppState().selectedEvent?.name ?? 'Mood Indigo'}</strong> (${AppState().selectedEvent?.listenerCount ?? 3400} active listeners)
      </div>
    </div>
    <div class="header-right">
      <div class="user-profile">👤 ${AppState().username}</div>
    </div>
  '''.toJS;
  
  final mainLayout = web.document.createElement('div') as web.HTMLDivElement;
  mainLayout.className = 'app-layout';
  
  final sidebar = web.document.createElement('div') as web.HTMLDivElement;
  sidebar.className = 'sidebar';
  sidebar.innerHTML = '''
    <ul class="nav">
      <li id="nav-home" class="active">🏠 Home</li>
      <li id="nav-search">🔍 Search</li>
      <li id="nav-events">🎉 Live Events</li>
      <li id="nav-queue">⚡ Live Queue</li>
      <li id="nav-library">📚 My Library</li>
    </ul>

    <div class="sidebar-section">
      <div class="section-title">SAVED PLAYLISTS</div>
      <ul class="playlist-quick-list" id="quick-playlists">
        <li data-id="p1">🔥 College Fest Bangers</li>
        <li data-id="p3">🌙 Late Night Chill</li>
        <li data-id="p2">💃 Navratri Garba Beats</li>
      </ul>
    </div>
  '''.toJS;
  
  final content = web.document.createElement('div') as web.HTMLDivElement;
  content.className = 'main-content';
  content.id = 'main-content';
  
  mainLayout.append(sidebar);
  mainLayout.append(content);
  
  appContainer.append(topBar);
  appContainer.append(mainLayout);
  
  // Attach Music Player
  appContainer.append(PlayerWidget.create());
  
  // Top Back Button Click
  topBar.querySelector('#btn-back')?.onClick.listen((_) {
    AppState().popScreen();
  });

  // Sidebar Nav clicks
  sidebar.querySelector('#nav-home')?.onClick.listen((_) => AppState().pushScreen('home'));
  sidebar.querySelector('#nav-search')?.onClick.listen((_) => AppState().pushScreen('search'));
  sidebar.querySelector('#nav-events')?.onClick.listen((_) => AppState().pushScreen('events'));
  sidebar.querySelector('#nav-queue')?.onClick.listen((_) => AppState().pushScreen('queue'));
  sidebar.querySelector('#nav-library')?.onClick.listen((_) => AppState().pushScreen('library'));

  // Sidebar Saved Playlists Clicks
  final quickItems = sidebar.querySelectorAll('#quick-playlists li');
  for (var i = 0; i < quickItems.length; i++) {
    final item = quickItems.item(i) as web.HTMLLIElement;
    final pId = item.getAttribute('data-id');
    item.onClick.listen((_) {
      final p = allPlaylists.firstWhere((pl) => pl.id == pId, orElse: () => allPlaylists[0]);
      AppState().openPlaylist(p);
    });
  }
  
  AppState().addListener(() {
    updateHeader(topBar);
    updateSidebar(sidebar);
    renderCurrentScreen();
  });
  
  renderCurrentScreen();
}

void updateHeader(web.HTMLDivElement topBar) {
  final backBtn = topBar.querySelector('#btn-back') as web.HTMLButtonElement?;
  if (backBtn != null) {
    if (AppState().canGoBack) {
      backBtn.classList.add('enabled');
    } else {
      backBtn.classList.remove('enabled');
    }
  }
}

void updateSidebar(web.HTMLDivElement sidebar) {
  final current = AppState().currentScreen;
  final navItems = sidebar.querySelectorAll('.nav li');
  for (var i = 0; i < navItems.length; i++) {
    (navItems.item(i) as web.Element).classList.remove('active');
  }
  sidebar.querySelector('#nav-$current')?.classList.add('active');
}

void renderCurrentScreen() {
  final content = web.document.querySelector('#main-content') as web.HTMLDivElement;
  content.innerHTML = ''''''.toJS;
  
  switch (AppState().currentScreen) {
    case 'home':
      content.append(HomeScreen.render());
      break;
    case 'queue':
      content.append(LiveQueueScreen.render());
      break;
    case 'events':
      content.append(EventsScreen.render());
      break;
    case 'search':
      content.append(SearchScreen.render());
      break;
    case 'library':
      content.append(LibraryScreen.render());
      break;
    case 'playlist_detail':
      content.append(PlaylistDetailScreen.render());
      break;
    default:
      content.append(HomeScreen.render());
  }
}
""",
    "screens/playlist_detail.dart": """import 'package:web/web.dart' as web;
import 'dart:js_interop';
import '../app/state.dart';

class PlaylistDetailScreen {
  static web.HTMLDivElement render() {
    final div = web.document.createElement('div') as web.HTMLDivElement;
    div.className = 'playlist-detail-screen';
    
    final state = AppState();
    final playlist = state.selectedPlaylist;

    if (playlist == null) {
      div.innerHTML = '<h2>No playlist selected</h2>'.toJS;
      return div;
    }

    final isSaved = state.savedPlaylists.contains(playlist);

    div.innerHTML = '''
      <div class="screen-header">
        ${state.canGoBack ? '<button class="back-link-btn" id="playlist-back-btn">← Back</button>' : ''}
        <h1>${playlist.name}</h1>
      </div>

      <div class="playlist-hero-header">
        <img src="${playlist.coverImage}" class="playlist-cover-hero" onerror="this.src='https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=400&q=80'">
        <div class="playlist-hero-info">
          <span class="category-pill">PUBLIC PLAYLIST</span>
          <h2>${playlist.name}</h2>
          <p class="desc">${playlist.description}</p>
          <div class="playlist-meta">🎵 ${playlist.songs.length} Tracks • Curated by TuneRequest Community</div>
          <div class="hero-actions">
            <button class="primary-btn play-all-btn" id="play-all-btn">▶ Play Playlist</button>
            <button class="save-playlist-btn ${isSaved ? 'saved' : ''}" id="save-pl-btn" style="width: auto; padding: 12px 20px;">
              ${isSaved ? '✓ Saved in Library' : '+ Save to Library'}
            </button>
          </div>
        </div>
      </div>

      <div class="section-container">
        <h2>Tracks in this Playlist</h2>
        <div class="queue-list" id="playlist-songs-list"></div>
      </div>
    '''.toJS;

    div.querySelector('#playlist-back-btn')?.onClick.listen((_) => state.popScreen());
    div.querySelector('#save-pl-btn')?.onClick.listen((_) => state.toggleSavePlaylist(playlist));

    final listContainer = div.querySelector('#playlist-songs-list') as web.HTMLDivElement;
    for (var song in playlist.songs) {
      final item = web.document.createElement('div') as web.HTMLDivElement;
      item.className = 'queue-card-item';
      final isLiked = state.likedSongs.contains(song);

      item.innerHTML = '''
        <img src="${song.coverImage}" class="queue-img" onerror="this.src='https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=400&q=80'">
        <div class="queue-details">
          <div class="song-title">${song.title}</div>
          <div class="song-sub">${song.artist} • ${song.album} (${song.formattedDuration})</div>
        </div>
        <button class="primary-btn play-track-btn">▶ Play</button>
        <button class="icon-btn like-track-btn">${isLiked ? '❤️' : '🤍'}</button>
        <button class="secondary-btn req-track-btn">⚡ Request</button>
      '''.toJS;

      item.querySelector('.play-track-btn')?.onClick.listen((_) {
        state.currentSong = song;
        state.isPlaying = true;
        state.notifyListeners();
      });

      item.querySelector('.like-track-btn')?.onClick.listen((_) {
        state.toggleLikeSong(song);
      });

      item.querySelector('.req-track-btn')?.onClick.listen((_) {
        state.addRequest(song);
        state.pushScreen('queue');
      });

      listContainer.append(item);
    }

    div.querySelector('#play-all-btn')?.onClick.listen((_) {
      if (playlist.songs.isNotEmpty) {
        state.currentSong = playlist.songs[0];
        state.isPlaying = true;
        state.notifyListeners();
      }
    });

    return div;
  }
}
""",
    "screens/home.dart": """import 'package:web/web.dart' as web;
import 'dart:js_interop';
import '../data/songs.dart';
import '../data/playlists.dart';
import '../app/state.dart';

class HomeScreen {
  static web.HTMLDivElement render() {
    final div = web.document.createElement('div') as web.HTMLDivElement;
    div.className = 'home-screen';
    
    final state = AppState();

    div.innerHTML = '''
      <div class="screen-header">
        ${state.canGoBack ? '<button class="back-link-btn" id="home-back-btn">← Back</button>' : ''}
        <h1>Welcome Back, ${state.username} 👋</h1>
      </div>

      <!-- Featured Live Event Banner -->
      <div class="hero-event-banner">
        <div class="banner-tag">🔥 ACTIVE COMMUNITY EVENT</div>
        <h2>${state.selectedEvent?.name ?? 'Mood Indigo Fest'}</h2>
        <p>Host: ${state.selectedEvent?.host} • 👥 ${state.selectedEvent?.listenerCount} Live Attendees</p>
        <button class="primary-btn" id="hero-join-btn">⚡ Join Stage Queue & Request Track</button>
      </div>

      <!-- Popular Songs Section -->
      <div class="section-container">
        <div class="section-header">
          <h2>Trending Tracks Across Stages</h2>
          <span class="sub-text">12 Songs Available</span>
        </div>
        <div class="song-grid" id="home-songs"></div>
      </div>

      <!-- Featured Playlists -->
      <div class="section-container">
        <div class="section-header">
          <h2>Popular Community Playlists</h2>
        </div>
        <div class="playlist-grid" id="home-playlists"></div>
      </div>
    '''.toJS;

    div.querySelector('#home-back-btn')?.onClick.listen((_) => state.popScreen());
    div.querySelector('#hero-join-btn')?.onClick.listen((_) => state.pushScreen('queue'));
    
    // Render Songs Grid
    final songsGrid = div.querySelector('#home-songs') as web.HTMLDivElement;
    for (var song in allSongs) {
      final card = web.document.createElement('div') as web.HTMLDivElement;
      card.className = 'song-card';
      final isLiked = state.likedSongs.contains(song);

      card.innerHTML = '''
        <div class="img-wrapper">
          <img src="${song.coverImage}" alt="${song.title}" loading="lazy" onerror="this.src='https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=400&q=80'">
          <button class="play-overlay-btn">▶</button>
        </div>
        <div class="song-meta">
          <div class="title" title="${song.title}">${song.title}</div>
          <div class="artist">${song.artist}</div>
          <div class="genre-tag">${song.genre}</div>
        </div>
        <div class="card-actions">
          <button class="icon-btn like-btn ${isLiked ? 'active' : ''}">${isLiked ? '❤️' : '🤍'}</button>
          <button class="icon-btn req-btn" title="Request for Live Stage">⚡ Request</button>
        </div>
      '''.toJS;
      
      card.querySelector('.img-wrapper')?.onClick.listen((_) {
        state.currentSong = song;
        state.isPlaying = true;
        state.notifyListeners();
      });

      card.querySelector('.like-btn')?.onClick.listen((e) {
        state.toggleLikeSong(song);
      });

      card.querySelector('.req-btn')?.onClick.listen((e) {
        state.addRequest(song);
        state.pushScreen('queue');
      });
      
      songsGrid.append(card);
    }

    // Render Playlists Grid
    final playlistGrid = div.querySelector('#home-playlists') as web.HTMLDivElement;
    for (var playlist in allPlaylists) {
      final card = web.document.createElement('div') as web.HTMLDivElement;
      card.className = 'playlist-card';
      final isSaved = state.savedPlaylists.contains(playlist);

      card.innerHTML = '''
        <img src="${playlist.coverImage}" alt="${playlist.name}" loading="lazy" onerror="this.src='https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=400&q=80'">
        <div class="title">${playlist.name}</div>
        <div class="desc">${playlist.description}</div>
        <button class="save-playlist-btn ${isSaved ? 'saved' : ''}">${isSaved ? '✓ Saved' : '+ Save Playlist'}</button>
      '''.toJS;

      card.querySelector('img')?.onClick.listen((_) {
        state.openPlaylist(playlist);
      });

      card.querySelector('.title')?.onClick.listen((_) {
        state.openPlaylist(playlist);
      });

      card.querySelector('.save-playlist-btn')?.onClick.listen((_) {
        state.toggleSavePlaylist(playlist);
      });

      playlistGrid.append(card);
    }
    
    return div;
  }
}
""",
    "screens/live_queue.dart": """import 'package:web/web.dart' as web;
import 'dart:js_interop';
import '../app/state.dart';
import '../data/songs.dart';

class LiveQueueScreen {
  static web.HTMLDivElement render() {
    final div = web.document.createElement('div') as web.HTMLDivElement;
    div.className = 'live-queue-screen';
    
    final state = AppState();
    final name = state.username ?? 'Vrish';

    div.innerHTML = '''
      <div class="screen-header">
        ${state.canGoBack ? '<button class="back-link-btn" id="queue-back-btn">← Back</button>' : ''}
        <h1>⚡ Live Queue & Upvotes</h1>
      </div>

      <div class="stage-info-bar">
        <div class="stage-title">STAGE: ${state.selectedEvent?.name}</div>
        <div class="live-pill">🔴 LIVE • ${state.selectedEvent?.listenerCount} ATTENDEES</div>
      </div>

      <div class="queue-layout">
        <div class="queue-main">
          <h2>Current Upvotes & Up Next</h2>
          <div class="queue-list" id="queue-items-container"></div>
        </div>

        <div class="queue-sidebar-form">
          <div class="form-card">
            <h3>🎵 Request a Track for DJ</h3>
            <p>Your request will broadcast live to all crowd members & DJ console.</p>
            
            <label>Select Track</label>
            <select id="request-select" class="form-input">
              ${allSongs.map((s) => '<option value="${s.id}">${s.title} — ${s.artist} (${s.genre})</option>').join('')}
            </select>

            <button id="request-btn" class="primary-btn full-width">🚀 Broadcast Request (+1 Vote)</button>
          </div>
        </div>
      </div>
    '''.toJS;

    div.querySelector('#queue-back-btn')?.onClick.listen((_) => state.popScreen());

    final listContainer = div.querySelector('#queue-items-container') as web.HTMLDivElement;

    if (state.queue.isEmpty) {
      listContainer.innerHTML = '<div class="empty-msg">No requests in queue yet. Be the first to request!</div>'.toJS;
    } else {
      for (var req in state.queue) {
        final item = web.document.createElement('div') as web.HTMLDivElement;
        item.className = 'queue-card-item';
        final hasVoted = req.requesters.contains(name);

        item.innerHTML = '''
          <img src="${req.song.coverImage}" class="queue-img" onerror="this.src='https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=400&q=80'">
          <div class="queue-details">
            <div class="song-title">${req.song.title}</div>
            <div class="song-sub">${req.song.artist} • ${req.song.genre}</div>
            <div class="requesters-tag">Requesters (${req.requesters.length}): <span>${req.requesters.join(', ')}</span></div>
          </div>
          <div class="queue-votes-side">
            <button class="upvote-btn ${hasVoted ? 'voted' : ''}" id="vote-btn-${req.id}">
              ${hasVoted ? '✓ Upvoted (1 Vote)' : '👍 +1 Upvote'}
            </button>
            <div class="vote-count"><strong>${req.requestCount}</strong> Total Votes</div>
          </div>
        '''.toJS;

        item.querySelector('#vote-btn-${req.id}')?.onClick.listen((_) {
          state.upvoteRequest(req);
        });

        listContainer.append(item);
      }
    }

    div.querySelector('#request-btn')?.onClick.listen((_) {
      final select = div.querySelector('#request-select') as web.HTMLSelectElement;
      final songId = select.value;
      final song = allSongs.firstWhere((s) => s.id == songId);
      
      state.addRequest(song);
    });

    return div;
  }
}
""",
    "screens/events.dart": """import 'package:web/web.dart' as web;
import 'dart:js_interop';
import '../data/events.dart';
import '../app/state.dart';

class EventsScreen {
  static web.HTMLDivElement render() {
    final div = web.document.createElement('div') as web.HTMLDivElement;
    div.className = 'events-screen';
    
    final state = AppState();

    div.innerHTML = '''
      <div class="screen-header">
        ${state.canGoBack ? '<button class="back-link-btn" id="events-back-btn">← Back</button>' : ''}
        <h1>🎉 Live Events & Stages Near You (${allEvents.length} Active Events)</h1>
      </div>

      <div class="events-grid" id="events-grid-container"></div>
    '''.toJS;

    div.querySelector('#events-back-btn')?.onClick.listen((_) => state.popScreen());

    final grid = div.querySelector('#events-grid-container') as web.HTMLDivElement;
    for (var event in allEvents) {
      final card = web.document.createElement('div') as web.HTMLDivElement;
      card.className = 'event-card';
      final isSelected = state.selectedEvent?.id == event.id;

      card.innerHTML = '''
        <img src="${event.bannerImage}" class="event-banner" onerror="this.src='https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=600&q=80'">
        <div class="event-body">
          <span class="category-pill">${event.category}</span>
          <div class="event-title">${event.name}</div>
          <div class="event-meta">📍 ${event.location} • 📅 ${event.date} (${event.time})</div>
          <div class="event-meta">🎧 Host: ${event.host}</div>
          <div class="event-meta">👥 ${event.listenerCount} Listeners active</div>
          <button class="primary-btn join-event-btn ${isSelected ? 'active-event' : ''}">
            ${isSelected ? '✓ Connected to Stage' : '⚡ Join Stage Queue'}
          </button>
        </div>
      '''.toJS;

      card.querySelector('.join-event-btn')?.onClick.listen((_) {
        state.selectedEvent = event;
        state.pushScreen('queue');
      });

      grid.append(card);
    }

    return div;
  }
}
""",
    "screens/library.dart": """import 'package:web/web.dart' as web;
import 'dart:js_interop';
import '../app/state.dart';
import '../data/artists.dart';

class LibraryScreen {
  static web.HTMLDivElement render() {
    final div = web.document.createElement('div') as web.HTMLDivElement;
    div.className = 'library-screen';
    
    final state = AppState();

    div.innerHTML = '''
      <div class="screen-header">
        ${state.canGoBack ? '<button class="back-link-btn" id="lib-back-btn">← Back</button>' : ''}
        <h1>📚 My Music Library</h1>
      </div>

      <div class="library-tabs">
        <button class="tab-btn active" id="tab-liked">Liked Songs (${state.likedSongs.length})</button>
        <button class="tab-btn" id="tab-playlists">Saved Playlists (${state.savedPlaylists.length})</button>
        <button class="tab-btn" id="tab-artists">Followed Artists (${state.followedArtists.length})</button>
        <button class="tab-btn" id="tab-recent">Recently Played (${state.recentlyPlayed.length})</button>
      </div>

      <div class="library-content" id="library-content-container"></div>
    '''.toJS;

    div.querySelector('#lib-back-btn')?.onClick.listen((_) => state.popScreen());

    final container = div.querySelector('#library-content-container') as web.HTMLDivElement;

    void renderLikedSongs() {
      container.innerHTML = ''''''.toJS;
      if (state.likedSongs.isEmpty) {
        container.innerHTML = '<div class="empty-msg">No liked songs yet. Explore Home to add favorites!</div>'.toJS;
        return;
      }
      final list = web.document.createElement('div') as web.HTMLDivElement;
      list.className = 'queue-list';
      for (var song in state.likedSongs) {
        final item = web.document.createElement('div') as web.HTMLDivElement;
        item.className = 'queue-card-item';
        item.innerHTML = '''
          <img src="${song.coverImage}" class="queue-img" onerror="this.src='https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=400&q=80'">
          <div class="queue-details">
            <div class="song-title">${song.title}</div>
            <div class="song-sub">${song.artist} • ${song.album}</div>
          </div>
          <button class="primary-btn play-lib-btn">▶ Play</button>
          <button class="icon-btn remove-like-btn">❤️ Liked</button>
        '''.toJS;
        item.querySelector('.play-lib-btn')?.onClick.listen((_) {
          state.currentSong = song;
          state.isPlaying = true;
          state.notifyListeners();
        });
        item.querySelector('.remove-like-btn')?.onClick.listen((_) {
          state.toggleLikeSong(song);
          renderLikedSongs();
        });
        list.append(item);
      }
      container.append(list);
    }

    renderLikedSongs();

    div.querySelector('#tab-liked')?.onClick.listen((e) {
      final tabs = div.querySelectorAll('.tab-btn');
      for (var i = 0; i < tabs.length; i++) {
        (tabs.item(i) as web.Element).classList.remove('active');
      }
      (e.currentTarget as web.Element).classList.add('active');
      renderLikedSongs();
    });

    div.querySelector('#tab-playlists')?.onClick.listen((e) {
      final tabs = div.querySelectorAll('.tab-btn');
      for (var i = 0; i < tabs.length; i++) {
        (tabs.item(i) as web.Element).classList.remove('active');
      }
      (e.currentTarget as web.Element).classList.add('active');
      container.innerHTML = ''''''.toJS;
      final grid = web.document.createElement('div') as web.HTMLDivElement;
      grid.className = 'playlist-grid';
      for (var p in state.savedPlaylists) {
        final card = web.document.createElement('div') as web.HTMLDivElement;
        card.className = 'playlist-card';
        card.innerHTML = '''
          <img src="${p.coverImage}" onerror="this.src='https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=400&q=80'">
          <div class="title">${p.name}</div>
          <div class="desc">${p.description} (${p.songs.length} Tracks)</div>
          <button class="primary-btn view-pl-btn full-width">▶ Open Playlist</button>
        '''.toJS;
        card.querySelector('.view-pl-btn')?.onClick.listen((_) {
          state.openPlaylist(p);
        });
        grid.append(card);
      }
      container.append(grid);
    });

    div.querySelector('#tab-artists')?.onClick.listen((e) {
      final tabs = div.querySelectorAll('.tab-btn');
      for (var i = 0; i < tabs.length; i++) {
        (tabs.item(i) as web.Element).classList.remove('active');
      }
      (e.currentTarget as web.Element).classList.add('active');
      container.innerHTML = ''''''.toJS;
      final grid = web.document.createElement('div') as web.HTMLDivElement;
      grid.className = 'playlist-grid';
      for (var artist in allArtists) {
        final card = web.document.createElement('div') as web.HTMLDivElement;
        card.className = 'playlist-card';
        final isFollowing = state.followedArtists.contains(artist);
        card.innerHTML = '''
          <img src="${artist.imageUrl}" style="border-radius: 50%;" onerror="this.src='https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&q=80'">
          <div class="title" style="text-align: center;">${artist.name}</div>
          <div class="desc" style="text-align: center;">${artist.genre}</div>
          <button class="save-playlist-btn ${isFollowing ? 'saved' : ''}">${isFollowing ? '✓ Following' : '+ Follow'}</button>
        '''.toJS;
        card.querySelector('.save-playlist-btn')?.onClick.listen((_) {
          state.toggleFollowArtist(artist);
        });
        grid.append(card);
      }
      container.append(grid);
    });

    div.querySelector('#tab-recent')?.onClick.listen((e) {
      final tabs = div.querySelectorAll('.tab-btn');
      for (var i = 0; i < tabs.length; i++) {
        (tabs.item(i) as web.Element).classList.remove('active');
      }
      (e.currentTarget as web.Element).classList.add('active');
      container.innerHTML = ''''''.toJS;
      final list = web.document.createElement('div') as web.HTMLDivElement;
      list.className = 'queue-list';
      for (var song in state.recentlyPlayed) {
        final item = web.document.createElement('div') as web.HTMLDivElement;
        item.className = 'queue-card-item';
        item.innerHTML = '''
          <img src="${song.coverImage}" class="queue-img" onerror="this.src='https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=400&q=80'">
          <div class="queue-details">
            <div class="song-title">${song.title}</div>
            <div class="song-sub">${song.artist} • ${song.album}</div>
          </div>
          <button class="primary-btn play-recent-btn">▶ Replay</button>
        '''.toJS;
        item.querySelector('.play-recent-btn')?.onClick.listen((_) {
          state.currentSong = song;
          state.isPlaying = true;
          state.notifyListeners();
        });
        list.append(item);
      }
      container.append(list);
    });

    return div;
  }
}
""",
    "screens/search.dart": """import 'package:web/web.dart' as web;
import 'dart:js_interop';
import '../data/songs.dart';
import '../app/state.dart';
import '../models/song.dart';

class SearchScreen {
  static web.HTMLDivElement render() {
    final div = web.document.createElement('div') as web.HTMLDivElement;
    div.className = 'search-screen';
    
    final state = AppState();

    div.innerHTML = '''
      <div class="screen-header">
        ${state.canGoBack ? '<button class="back-link-btn" id="search-back-btn">← Back</button>' : ''}
        <h1>🔍 Search Music & Artists</h1>
      </div>

      <div class="search-bar-container">
        <input type="text" id="search-input" placeholder="Type song title, artist, or genre..." class="form-input search-input">
      </div>

      <div class="search-results-grid" id="search-results"></div>
    '''.toJS;

    div.querySelector('#search-back-btn')?.onClick.listen((_) => state.popScreen());

    final resultsContainer = div.querySelector('#search-results') as web.HTMLDivElement;
    final input = div.querySelector('#search-input') as web.HTMLInputElement;

    void displayResults(List<Song> songs) {
      resultsContainer.innerHTML = ''''''.toJS;
      for (var song in songs) {
        final card = web.document.createElement('div') as web.HTMLDivElement;
        card.className = 'song-card';
        card.innerHTML = '''
          <img src="${song.coverImage}" onerror="this.src='https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=400&q=80'">
          <div class="title">${song.title}</div>
          <div class="artist">${song.artist}</div>
        '''.toJS;
        card.onClick.listen((_) {
          state.currentSong = song;
          state.isPlaying = true;
          state.notifyListeners();
        });
        resultsContainer.append(card);
      }
    }

    displayResults(allSongs);

    input.onInput.listen((_) {
      final query = input.value.toLowerCase().trim();
      if (query.isEmpty) {
        displayResults(allSongs);
      } else {
        final filtered = allSongs.where((s) =>
          s.title.toLowerCase().contains(query) ||
          s.artist.toLowerCase().contains(query) ||
          s.genre.toLowerCase().contains(query)
        ).toList();
        displayResults(filtered);
      }
    });

    return div;
  }
}
""",
    "widgets/player.dart": """import 'package:web/web.dart' as web;
import 'dart:js_interop';
import '../app/state.dart';

class PlayerWidget {
  static web.HTMLDivElement create() {
    final player = web.document.createElement('div') as web.HTMLDivElement;
    player.className = 'music-player';
    player.id = 'music-player';
    
    AppState().addListener(() {
      updatePlayer(player);
    });
    
    updatePlayer(player);
    return player;
  }
  
  static void updatePlayer(web.HTMLDivElement player) {
    final state = AppState();
    if (state.currentSong == null) {
      player.innerHTML = '<div class="empty-player">Select a track to start playback</div>'.toJS;
      return;
    }
    
    final song = state.currentSong!;
    final isLiked = state.likedSongs.contains(song);

    player.innerHTML = '''
      <div class="player-left">
        <img src="${song.coverImage}" alt="Cover" onerror="this.src='https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=400&q=80'">
        <div class="player-song-meta">
          <div class="title">${song.title}</div>
          <div class="artist">${song.artist}</div>
        </div>
        <button class="icon-btn player-like-btn">${isLiked ? '❤️' : '🤍'}</button>
      </div>
      <div class="player-center">
        <div class="controls">
          <button id="btn-prev">⏮</button>
          <button id="btn-play" class="play-pause-circle">${state.isPlaying ? '⏸' : '▶'}</button>
          <button id="btn-next">⏭</button>
        </div>
        <div class="progress-container">
          <span class="time-label">1:12</span>
          <div class="progress-bar">
            <div class="progress" style="width: ${state.currentProgress}%"></div>
          </div>
          <span class="time-label">${song.formattedDuration}</span>
        </div>
      </div>
      <div class="player-right">
        <button class="secondary-btn req-stage-btn" id="player-req-btn">⚡ Request for Live Stage</button>
      </div>
    '''.toJS;
    
    player.querySelector('#btn-play')?.onClick.listen((_) {
      state.isPlaying = !state.isPlaying;
      state.notifyListeners();
    });

    player.querySelector('.player-like-btn')?.onClick.listen((_) {
      state.toggleLikeSong(song);
    });

    player.querySelector('#player-req-btn')?.onClick.listen((_) {
      state.addRequest(song);
      state.pushScreen('queue');
    });
  }
}
"""
}

for rel_path, content in files.items():
    write_file(os.path.join(base_dir, rel_path), content)

print("Updated Dart files with sidebar saved playlist click navigation successfully generated!")
