import 'package:web/web.dart' as web;
import 'dart:js_interop';
import '../app/state.dart';

class RealtimeService {
  static web.BroadcastChannel? _channel;
  
  static void init(Function(String) onMessage) {
    try {
      _channel = web.BroadcastChannel('tunerequest_live_v4');
      _channel!.onmessage = ((web.MessageEvent event) {
        onMessage(event.data.toString());
      }).toJS;

      web.window.addEventListener('storage', ((web.StorageEvent event) {
        if (event.key == 'tune_queue_data') {
          AppState().refreshFromStorage();
          AppState().notifyListeners();
        }
      }).toJS);
    } catch (e) {
      print('Realtime service init error: $e');
    }
  }
  
  static void broadcastQueue(String queueJsonPayload) {
    try {
      _channel?.postMessage(queueJsonPayload.toJS);
    } catch (e) {
      print('Broadcast error: $e');
    }
  }
}
