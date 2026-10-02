class Artist {
  final String id;
  final String name;
  final String imageUrl;
  final String genre;
  final int followers;
  bool isFollowing;

  Artist({
    required this.id,
    required this.name,
    required this.imageUrl,
    required this.genre,
    required this.followers,
    this.isFollowing = false,
  });
}