import '../models/playlist.dart';
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
];