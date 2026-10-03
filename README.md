<img width="1190" height="765" alt="Screenshot 2026-10-03 at 12 49 14 PM" src="https://github.com/user-attachments/assets/70b510a5-62b9-49bd-a2ff-4e36584d1206" />
<img width="1181" height="754" alt="Screenshot 2026-10-03 at 12 49 37 PM" src="https://github.com/user-attachments/assets/509a9e7a-8d50-413f-97b5-083d1de8ba4b" />
<img width="1186" height="752" alt="Screenshot 2026-10-03 at 12 49 53 PM" src="https://github.com/user-attachments/assets/f14db1c6-b403-455c-bc6d-ff020045dbe1" />
<img width="1190" height="757" alt="Screenshot 2026-10-03 at 12 49 46 PM" src="https://github.com/user-attachments/assets/17a84578-195d-4484-a79f-676bcf75f813" />
<img width="1200" height="770" alt="Screenshot 2026-10-03 at 12 50 01 PM" src="https://github.com/user-attachments/assets/f8bf7692-811d-42ae-ac45-47166b1c22a7" />
<img width="1199" height="765" alt="Screenshot 2026-10-03 at 12 50 14 PM" src="https://github.com/user-attachments/assets/16102b11-b49d-48d5-9a6b-f53450f2fb45" />
<img width="1190" height="761" alt="Screenshot 2026-10-03 at 12 50 21 PM" src="https://github.com/user-attachments/assets/2af524d2-6037-49bb-8c39-dcd09c54967f" />
<img width="1190" height="761" alt="Screenshot 2026-10-03 at 12 50 21 PM" src="https://github.com/user-attachments/assets/4e396aa1-606c-4fcf-8c16-9c6e40dbcc74" /><img width="1199" height="765" alt="Screenshot 2026-10-03 at 12 50 14 PM" src="https://github.com/user-attachments/assets/a1f4ee0d-46f4-4122-8d68-00786bcffcbd" />![Uploading Screenshot 2026-10-03 at 12.50.43 PM.png…]()
# 🎵 TuneRequest — Real-Time Community Music & Live Event Queue Platform

A web application built using **100% Pure Dart for Web** (`package:web` and native DOM APIs).

---

## 📌 Problem Statement & Technical Justification

### Problem Statement
Modern music streaming platforms (such as Spotify, Apple Music, or YouTube Music) are designed strictly for **single-listener or isolated session experiences**. In live crowd environments—such as college cultural fests (e.g., IIT Bombay Mood Indigo, DU Spring Fest), wedding sangeets, club DJ nights, and community lounges—attendees face several major challenges:

1. **DJ Booth Chaos:** Attendees crowd the DJ console or shout requests over loud speakers, causing disruption and friction for the performer.
2. **Lack of Crowd Democracy:** Traditional event queues rely on verbal requests or paper slips, giving DJ set planners no structured signal regarding crowd preferences or track popularity.
3. **No Real-Time Shared Visibility:** Attendees cannot see what tracks are currently queued, who requested them, or how many other attendees want to hear the same track.

### Proposed Solution & Justification
**TuneRequest** solves this by providing a lightweight, zero-install, crowd-powered live song request and real-time upvoting platform:
- **Crowd Democracy:** Attendees search the catalogue, request songs, and upvote existing requests. Tracks automatically re-order in real time based on total upvotes (`1 vote per user`).
- **Real-Time Sync Without Complex Backends:** Using browser-native `BroadcastChannel` and `LocalStorage` sync APIs, live queues update across all connected crowd devices instantly with sub-millisecond latency—eliminating the overhead and cost of external database clusters like Firebase or Supabase.
- **Pure Dart Architecture:** The entire application logic, UI renderer, state manager, and event dispatch loop are written strictly in **Dart**, compiling directly to optimized JavaScript.

---

## 🚀 How to Run TuneRequest in Visual Studio Code (VS Code)

Follow these simple steps to run and test the project inside **VS Code**:

### Option A: Using VS Code Integrated Terminal (Recommended & Fast)

1. **Open the Project in VS Code:**
   - Launch VS Code.
   - Click `File > Open Folder...` (or `Cmd + O` on Mac) and select the `tunerequest` project folder.

2. **Open the Integrated Terminal:**
   - Press `Ctrl + ~` (or `Cmd + ~` on Mac), or go to `Terminal > New Terminal` in the top menu.

3. **Compile and Run Server:**
   - In the terminal, compile the Dart application to JavaScript:
     ```bash
     dart compile js web/main.dart -o web/main.dart.js
     ```
   - Start the local HTTP web server:
     ```bash
     python3 -m http.server 8085 --directory web
     ```

4. **Open in Browser:**
   - Open your browser and navigate to:
     **`http://localhost:8085`**

---

### Option B: Using `webdev`

If you have `webdev` installed globally in Dart:

1. Open the VS Code Terminal (`Ctrl + ~`).
2. Run:
   ```bash
   dart pub global activate webdev
   webdev serve web:8085
   ```
3. Open `http://localhost:8085` in your browser.

---

## ⚡ How to Demonstrate Real-Time Queue Updates (College Viva Guide)

You can demonstrate live multi-user synchronization across multiple devices or browser tabs **without needing a remote server**:

1. **Open Tab 1 (DJ / Stage Console):**
   - Open `http://localhost:8085` in Browser Tab 1.
   - Enter your name (e.g., `DJ Host`) and navigate to **⚡ Live Queue**.

2. **Open Tab 2 (Attendee Device):**
   - Open `http://localhost:8085` in Browser Tab 2 (or a separate Private/Incognito window).
   - Enter a different name (e.g., `Ayaan`).
   - Navigate to **⚡ Live Queue**.

3. **Trigger Real-Time Upvotes:**
   - In **Tab 2**, click **`👍 +1 Upvote`** on any song request or request a new track.
   - **Observe Tab 1:** Notice how **Tab 1** instantly updates its vote count, requester list, and queue position in real-time **without refreshing the page**!

---

## 🎨 Key Project Features

- **🏠 Home Screen:** Hero banner featuring active fests, trending Indian music catalogue (Bollywood, Punjabi, Telugu, Tamil, Malayalam, Marathi, Indie), and popular community playlists.
- **⚡ Live Queue & Voting:** Real-time upvoting queue sorted dynamically by total crowd votes (`1 vote per user` restriction enforced).
- **🎉 Live Events:** Browse 8+ active events across Mumbai, Bengaluru, Udaipur, Pune, Delhi, and Goa.
- **📚 My Music Library:** Organized tabs for Liked Songs, Saved Playlists, Followed Artists, and Recently Played tracks.
- **🎵 Music Player:** Persistent bottom audio player with progress bar, volume controls, play/pause state, and quick-request shortcuts.
- **🔍 Search:** Live filtering across songs, artists, albums, and genres.
- **⬅️ Full Back Button Navigation:** Dynamic navigation stack allowing seamless back/forward browser-like navigation (`AppState.pushScreen` & `AppState.popScreen`).

---

## ⚙️ Technology Stack & Compliance

| Requirement | Implementation Detail | Status |
| :--- | :--- | :---: |
| **Language** | Pure Dart (`dart:js_interop`, `package:web`) | ✅ Compliant |
| **Frameworks** | No Flutter, No React, No Vue, No Angular | ✅ Compliant |
| **Backend** | Zero external backends (No Firebase, Supabase, Node.js) | ✅ Compliant |
| **Styling** | Vanilla CSS (`web/styles.css`) | ✅ Compliant |
| **Real-Time Engine** | Native `BroadcastChannel` + `LocalStorage` Sync | ✅ Compliant |

---

## 📂 Project Structure

```
tunerequest/
├── README.md                  # Project documentation & problem statement
├── pubspec.yaml               # Dart web package dependencies
├── web/
│   ├── index.html             # Minimal HTML bootstrap container
│   ├── main.dart              # Dart entry point
│   ├── main.dart.js           # Compiled JavaScript output
│   └── styles.css             # Vanilla CSS design system
└── lib/
    ├── main.dart              # Core app initialization & layout router
    ├── app/
    │   └── state.dart         # Central AppState & 1-vote sync logic
    ├── models/
    │   ├── song.dart          # Track model
    │   ├── artist.dart        # Artist model
    │   ├── playlist.dart      # Playlist model
    │   ├── event.dart         # Live event model
    │   └── song_request.dart  # Song request & upvote model
    ├── data/
    │   ├── songs.dart         # Indian music catalogue
    │   ├── artists.dart       # Artist catalogue
    │   ├── playlists.dart     # Community playlists
    │   └── events.dart        # Live stages data
    ├── screens/
    │   ├── home.dart          # Discovery dashboard
    │   ├── live_queue.dart    # Live crowd queue & voting screen
    │   ├── events.dart        # Live event stages
    │   ├── library.dart       # User library tabs
    │   ├── search.dart        # Search screen
    │   └── playlist_detail.dart # Direct playlist view screen
    ├── widgets/
    │   └── player.dart        # Persistent bottom music player
    └── services/
        ├── storage.dart       # LocalStorage wrapper
        └── realtime.dart      # BroadcastChannel & storage event listener
```

---

## 👥 Author & Repository

- **GitHub Repository:** [https://github.com/vrish-thadani/TuneRequest.git](https://github.com/vrish-thadani/TuneRequest.git)
- **Author:** Vrish Thadani
