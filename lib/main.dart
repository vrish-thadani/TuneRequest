import 'package:web/web.dart' as web;
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

  final ticker = topBar.querySelector('.live-event-ticker');
  if (ticker != null) {
    ticker.innerHTML = '🔴 LIVE STAGE: <strong>${AppState().selectedEvent?.name ?? 'Mood Indigo'}</strong> (${AppState().selectedEvent?.listenerCount ?? 3400} active listeners)'.toJS;
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
