class Song {
  final String id;
  final String title;
  final String artist;
  final String album;
  final String genre;
  final String language;
  final int duration;
  final String coverImage;
  bool isLiked;

  Song({
    required this.id,
    required this.title,
    required this.artist,
    required this.album,
    required this.genre,
    required this.language,
    required this.duration,
    required this.coverImage,
    this.isLiked = false,
  });

  Map<String, dynamic> toJson() => {
    'id': id,
    'title': title,
    'artist': artist,
    'album': album,
    'genre': genre,
    'language': language,
    'duration': duration,
    'coverImage': coverImage,
    'isLiked': isLiked,
  };

  factory Song.fromJson(Map<String, dynamic> json) => Song(
    id: json['id'] as String,
    title: json['title'] as String,
    artist: json['artist'] as String,
    album: json['album'] as String,
    genre: json['genre'] as String,
    language: json['language'] as String,
    duration: json['duration'] as int,
    coverImage: json['coverImage'] as String,
    isLiked: json['isLiked'] as bool? ?? false,
  );

  String get formattedDuration {
    final mins = duration ~/ 60;
    final secs = (duration % 60).toString().padLeft(2, '0');
    return '$mins:$secs';
  }
}