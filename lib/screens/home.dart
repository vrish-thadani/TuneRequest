import 'package:web/web.dart' as web;
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
