import 'package:web/web.dart' as web;
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
