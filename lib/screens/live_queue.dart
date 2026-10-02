import 'package:web/web.dart' as web;
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
