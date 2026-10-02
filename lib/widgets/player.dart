import 'package:web/web.dart' as web;
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
