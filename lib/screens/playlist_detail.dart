import 'package:web/web.dart' as web;
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
