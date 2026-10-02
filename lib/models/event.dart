class Event {
  final String id;
  final String name;
  final String location;
  final String date;
  final String time;
  final String host;
  final int listenerCount;
  final String category;
  final String currentSongId;
  final String bannerImage;

  Event({
    required this.id,
    required this.name,
    required this.location,
    required this.date,
    required this.time,
    required this.host,
    required this.listenerCount,
    required this.category,
    required this.currentSongId,
    required this.bannerImage,
  });
}