import 'package:web/web.dart' as web;
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
