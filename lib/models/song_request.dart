import 'song.dart';

class SongRequest {
  final String id;
  final Song song;
  final List<String> requesters;
  int requestCount;
  final String timestamp;

  SongRequest({
    required this.id,
    required this.song,
    required this.requesters,
    this.requestCount = 1,
    required this.timestamp,
  });

  Map<String, dynamic> toJson() => {
    'id': id,
    'song': song.toJson(),
    'requesters': requesters,
    'requestCount': requestCount,
    'timestamp': timestamp,
  };

  factory SongRequest.fromJson(Map<String, dynamic> json) => SongRequest(
    id: json['id'] as String,
    song: Song.fromJson(Map<String, dynamic>.from(json['song'] as Map)),
    requesters: List<String>.from(json['requesters'] as List),
    requestCount: json['requestCount'] as int,
    timestamp: json['timestamp'] as String? ?? 'Just now',
  );
}