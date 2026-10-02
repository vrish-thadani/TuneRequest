import 'package:web/web.dart' as web;

class StorageService {
  static void setItem(String key, String value) {
    web.window.localStorage.setItem(key, value);
  }
  
  static String? getItem(String key) {
    return web.window.localStorage.getItem(key);
  }

  static void saveUsername(String name) {
    setItem('username', name);
  }

  static String? getUsername() {
    return getItem('username');
  }
}
