import 'package:web/web.dart' as web;
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
          state.currentSecondsElapsed = 0;
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
