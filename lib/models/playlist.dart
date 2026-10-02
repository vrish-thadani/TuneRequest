import 'song.dart';

class Playlist {
  final String id;
  final String name;
  final String description;
  final String coverImage;
  final List<Song> songs;
  bool isSaved;

  Playlist({
    required this.id,
    required this.name,
    required this.description,
    required this.coverImage,
    required this.songs,
    this.isSaved = false,
  });
}