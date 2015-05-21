{
  'variables': {
    'app_sources': [
      'atom/app/atom_main.cc',
      'atom/app/atom_main.h',
    ],
    'bundle_sources': [
      'atom/browser/resources/mac/atom.icns',
    ],
    'coffee_sources': [
      'atom/browser/api/lib/app.coffee',
      'atom/browser/api/lib/atom-delegate.coffee',
      'atom/browser/api/lib/auto-updater.coffee',
      'atom/browser/api/lib/browser-window.coffee',
      'atom/browser/api/lib/content-tracing.coffee',
      'atom/browser/api/lib/dialog.coffee',
      'atom/browser/api/lib/global-shortcut.coffee',
      'atom/browser/api/lib/ipc.coffee',
      'atom/browser/api/lib/menu.coffee',
      'atom/browser/api/lib/menu-item.coffee',
      'atom/browser/api/lib/navigation-controller.coffee',
      'atom/browser/api/lib/power-monitor.coffee',
      'atom/browser/api/lib/protocol.coffee',
      'atom/browser/api/lib/screen.coffee',
      'atom/browser/api/lib/tray.coffee',
      'atom/browser/api/lib/web-contents.coffee',
      'atom/browser/lib/chrome-extension.coffee',
      'atom/browser/lib/guest-view-manager.coffee',
      'atom/browser/lib/guest-window-manager.coffee',
      'atom/browser/lib/init.coffee',
      'atom/browser/lib/objects-registry.coffee',
      'atom/browser/lib/rpc-server.coffee',
      'atom/common/api/lib/callbacks-registry.coffee',
      'atom/common/api/lib/clipboard.coffee',
      'atom/common/api/lib/crash-reporter.coffee',
      'atom/common/api/lib/id-weak-map.coffee',
      'atom/common/api/lib/native-image.coffee',
      'atom/common/api/lib/shell.coffee',
      'atom/common/lib/init.coffee',
      'atom/renderer/lib/chrome-api.coffee',
      'atom/renderer/lib/init.coffee',
      'atom/renderer/lib/inspector.coffee',
      'atom/renderer/lib/override.coffee',
      'atom/renderer/lib/web-view/guest-view-internal.coffee',
      'atom/renderer/lib/web-view/web-view.coffee',
      'atom/renderer/lib/web-view/web-view-attributes.coffee',
      'atom/renderer/lib/web-view/web-view-constants.coffee',
      'atom/renderer/api/lib/ipc.coffee',
      'atom/renderer/api/lib/remote.coffee',
      'atom/renderer/api/lib/screen.coffee',
      'atom/renderer/api/lib/web-frame.coffee',
    ],
    'coffee2c_sources': [
      'atom/common/lib/asar.coffee',
      'atom/common/lib/asar_init.coffee',
    ],
    'lib_sources': [
      'atom/app/atom_content_client.cc',
      'atom/app/atom_content_client.h',
      'atom/app/atom_main_args.cc',
      'atom/app/atom_main_args.h',
      'atom/app/atom_main_delegate.cc',
      'atom/app/atom_main_delegate.h',
      'atom/app/atom_main_delegate_mac.mm',
      'atom/app/node_main.cc',
      'atom/app/node_main.h',
      'atom/browser/api/atom_api_app.cc',
      'atom/browser/api/atom_api_app.h',
      'atom/browser/api/atom_api_auto_updater.cc',
      'atom/browser/api/atom_api_auto_updater.h',
      'atom/browser/api/atom_api_content_tracing.cc',
      'atom/browser/api/atom_api_dialog.cc',
      'atom/browser/api/atom_api_global_shortcut.cc',
      'atom/browser/api/atom_api_global_shortcut.h',
      'atom/browser/api/atom_api_menu.cc',
      'atom/browser/api/atom_api_menu.h',
      'atom/browser/api/atom_api_menu_views.cc',
      'atom/browser/api/atom_api_menu_views.h',
      'atom/browser/api/atom_api_menu_mac.h',
      'atom/browser/api/atom_api_menu_mac.mm',
      'atom/browser/api/atom_api_power_monitor.cc',
      'atom/browser/api/atom_api_power_monitor.h',
      'atom/browser/api/atom_api_protocol.cc',
      'atom/browser/api/atom_api_protocol.h',
      'atom/browser/api/atom_api_screen.cc',
      'atom/browser/api/atom_api_screen.h',
      'atom/browser/api/atom_api_tray.cc',
      'atom/browser/api/atom_api_tray.h',
      'atom/browser/api/atom_api_web_contents.cc',
      'atom/browser/api/atom_api_web_contents.h',
      'atom/browser/api/atom_api_web_view_manager.cc',
      'atom/browser/api/atom_api_window.cc',
      'atom/browser/api/atom_api_window.h',
      'atom/browser/api/event.cc',
      'atom/browser/api/event.h',
      'atom/browser/api/event_emitter.cc',
      'atom/browser/api/event_emitter.h',
      'atom/browser/auto_updater.cc',
      'atom/browser/auto_updater.h',
      'atom/browser/auto_updater_delegate.h',
      'atom/browser/auto_updater_linux.cc',
      'atom/browser/auto_updater_mac.mm',
      'atom/browser/auto_updater_win.cc',
      'atom/browser/atom_access_token_store.cc',
      'atom/browser/atom_access_token_store.h',
      'atom/browser/atom_browser_client.cc',
      'atom/browser/atom_browser_client.h',
      'atom/browser/atom_browser_context.cc',
      'atom/browser/atom_browser_context.h',
      'atom/browser/atom_browser_main_parts.cc',
      'atom/browser/atom_browser_main_parts.h',
      'atom/browser/atom_browser_main_parts_linux.cc',
      'atom/browser/atom_browser_main_parts_mac.mm',
      'atom/browser/atom_javascript_dialog_manager.cc',
      'atom/browser/atom_javascript_dialog_manager.h',
      'atom/browser/atom_quota_permission_context.cc',
      'atom/browser/atom_quota_permission_context.h',
      'atom/browser/atom_resource_dispatcher_host_delegate.cc',
      'atom/browser/atom_resource_dispatcher_host_delegate.h',
      'atom/browser/atom_speech_recognition_manager_delegate.cc',
      'atom/browser/atom_speech_recognition_manager_delegate.h',
      'atom/browser/browser.cc',
      'atom/browser/browser.h',
      'atom/browser/browser_linux.cc',
      'atom/browser/browser_mac.mm',
      'atom/browser/browser_win.cc',
      'atom/browser/browser_observer.h',
      'atom/browser/javascript_environment.cc',
      'atom/browser/javascript_environment.h',
      'atom/browser/mac/atom_application.h',
      'atom/browser/mac/atom_application.mm',
      'atom/browser/mac/atom_application_delegate.h',
      'atom/browser/mac/atom_application_delegate.mm',
      'atom/browser/native_window.cc',
      'atom/browser/native_window.h',
      'atom/browser/native_window_views.cc',
      'atom/browser/native_window_views.h',
      'atom/browser/native_window_mac.h',
      'atom/browser/native_window_mac.mm',
      'atom/browser/native_window_observer.h',
      'atom/browser/net/adapter_request_job.cc',
      'atom/browser/net/adapter_request_job.h',
      'atom/browser/net/asar/asar_protocol_handler.cc',
      'atom/browser/net/asar/asar_protocol_handler.h',
      'atom/browser/net/asar/url_request_asar_job.cc',
      'atom/browser/net/asar/url_request_asar_job.h',
      'atom/browser/net/atom_url_request_job_factory.cc',
      'atom/browser/net/atom_url_request_job_factory.h',
      'atom/browser/net/http_protocol_handler.cc',
      'atom/browser/net/http_protocol_handler.h',            
      'atom/browser/net/url_request_string_job.cc',
      'atom/browser/net/url_request_string_job.h',
      'atom/browser/net/url_request_buffer_job.cc',
      'atom/browser/net/url_request_buffer_job.h',
      'atom/browser/ui/accelerator_util.cc',
      'atom/browser/ui/accelerator_util.h',
      'atom/browser/ui/accelerator_util_mac.mm',
      'atom/browser/ui/accelerator_util_views.cc',
      'atom/browser/ui/cocoa/atom_menu_controller.h',
      'atom/browser/ui/cocoa/atom_menu_controller.mm',
      'atom/browser/ui/cocoa/event_processing_window.h',
      'atom/browser/ui/cocoa/event_processing_window.mm',
      'atom/browser/ui/file_dialog.h',
      'atom/browser/ui/file_dialog_gtk.cc',
      'atom/browser/ui/file_dialog_mac.mm',
      'atom/browser/ui/file_dialog_win.cc',
      'atom/browser/ui/message_box.h',
      'atom/browser/ui/message_box_mac.mm',
      'atom/browser/ui/message_box_views.cc',
      'atom/browser/ui/tray_icon.cc',
      'atom/browser/ui/tray_icon.h',
      'atom/browser/ui/tray_icon_gtk.cc',
      'atom/browser/ui/tray_icon_gtk.h',
      'atom/browser/ui/tray_icon_cocoa.h',
      'atom/browser/ui/tray_icon_cocoa.mm',
      'atom/browser/ui/tray_icon_observer.h',
      'atom/browser/ui/tray_icon_win.cc',
      'atom/browser/ui/views/frameless_view.cc',
      'atom/browser/ui/views/frameless_view.h',
      'atom/browser/ui/views/global_menu_bar_x11.cc',
      'atom/browser/ui/views/global_menu_bar_x11.h',
      'atom/browser/ui/views/menu_bar.cc',
      'atom/browser/ui/views/menu_bar.h',
      'atom/browser/ui/views/menu_delegate.cc',
      'atom/browser/ui/views/menu_delegate.h',
      'atom/browser/ui/views/menu_layout.cc',
      'atom/browser/ui/views/menu_layout.h',
      'atom/browser/ui/views/submenu_button.cc',
      'atom/browser/ui/views/submenu_button.h',
      'atom/browser/ui/views/win_frame_view.cc',
      'atom/browser/ui/views/win_frame_view.h',
      'atom/browser/ui/win/notify_icon_host.cc',
      'atom/browser/ui/win/notify_icon_host.h',
      'atom/browser/ui/win/notify_icon.cc',
      'atom/browser/ui/win/notify_icon.h',
      'atom/browser/ui/x/window_state_watcher.cc',
      'atom/browser/ui/x/window_state_watcher.h',
      'atom/browser/ui/x/x_window_utils.cc',
      'atom/browser/ui/x/x_window_utils.h',
      'atom/browser/web_view_manager.cc',
      'atom/browser/web_view_manager.h',
      'atom/browser/web_dialog_helper.cc',
      'atom/browser/web_dialog_helper.h',
      'atom/browser/window_list.cc',
      'atom/browser/window_list.h',
      'atom/browser/window_list_observer.h',
      'atom/common/api/api_messages.h',
      'atom/common/api/atom_api_asar.cc',
      'atom/common/api/atom_api_clipboard.cc',
      'atom/common/api/atom_api_crash_reporter.cc',
      'atom/common/api/atom_api_id_weak_map.cc',
      'atom/common/api/atom_api_id_weak_map.h',
      'atom/common/api/atom_api_native_image.cc',
      'atom/common/api/atom_api_native_image.h',
      'atom/common/api/atom_api_native_image_mac.mm',
      'atom/common/api/atom_api_shell.cc',
      'atom/common/api/atom_api_v8_util.cc',
      'atom/common/api/atom_bindings.cc',
      'atom/common/api/atom_bindings.h',
      'atom/common/api/object_life_monitor.cc',
      'atom/common/api/object_life_monitor.h',
      'atom/common/asar/archive.cc',
      'atom/common/asar/archive.h',
      'atom/common/asar/asar_util.cc',
      'atom/common/asar/asar_util.h',
      'atom/common/asar/scoped_temporary_file.cc',
      'atom/common/asar/scoped_temporary_file.h',
      'atom/common/common_message_generator.cc',
      'atom/common/common_message_generator.h',
      'atom/common/crash_reporter/crash_reporter.cc',
      'atom/common/crash_reporter/crash_reporter.h',
      'atom/common/crash_reporter/crash_reporter_linux.cc',
      'atom/common/crash_reporter/crash_reporter_linux.h',
      'atom/common/crash_reporter/crash_reporter_mac.h',
      'atom/common/crash_reporter/crash_reporter_mac.mm',
      'atom/common/crash_reporter/crash_reporter_win.cc',
      'atom/common/crash_reporter/crash_reporter_win.h',
      'atom/common/crash_reporter/linux/crash_dump_handler.cc',
      'atom/common/crash_reporter/linux/crash_dump_handler.h',
      'atom/common/crash_reporter/win/crash_service.cc',
      'atom/common/crash_reporter/win/crash_service.h',
      'atom/common/crash_reporter/win/crash_service_main.cc',
      'atom/common/crash_reporter/win/crash_service_main.h',
      'atom/common/draggable_region.cc',
      'atom/common/draggable_region.h',
      'atom/common/google_api_key.h',
      'atom/common/linux/application_info.cc',
      'atom/common/native_mate_converters/accelerator_converter.cc',
      'atom/common/native_mate_converters/accelerator_converter.h',
      'atom/common/native_mate_converters/file_path_converter.h',
      'atom/common/native_mate_converters/gfx_converter.cc',
      'atom/common/native_mate_converters/gfx_converter.h',
      'atom/common/native_mate_converters/gurl_converter.h',
      'atom/common/native_mate_converters/image_converter.cc',
      'atom/common/native_mate_converters/image_converter.h',
      'atom/common/native_mate_converters/string16_converter.h',
      'atom/common/native_mate_converters/v8_value_converter.cc',
      'atom/common/native_mate_converters/v8_value_converter.h',
      'atom/common/native_mate_converters/value_converter.cc',
      'atom/common/native_mate_converters/value_converter.h',
      'atom/common/node_bindings.cc',
      'atom/common/node_bindings.h',
      'atom/common/node_bindings_linux.cc',
      'atom/common/node_bindings_linux.h',
      'atom/common/node_bindings_mac.cc',
      'atom/common/node_bindings_mac.h',
      'atom/common/node_bindings_win.cc',
      'atom/common/node_bindings_win.h',
      'atom/common/node_includes.h',
      'atom/common/options_switches.cc',
      'atom/common/options_switches.h',
      'atom/common/platform_util.h',
      'atom/common/platform_util_linux.cc',
      'atom/common/platform_util_mac.mm',
      'atom/common/platform_util_win.cc',
      'atom/renderer/api/atom_api_renderer_ipc.cc',
      'atom/renderer/api/atom_api_spell_check_client.cc',
      'atom/renderer/api/atom_api_spell_check_client.h',
      'atom/renderer/api/atom_api_web_frame.cc',
      'atom/renderer/api/atom_api_web_frame.h',
      'atom/renderer/atom_render_view_observer.cc',
      'atom/renderer/atom_render_view_observer.h',
      'atom/renderer/atom_renderer_client.cc',
      'atom/renderer/atom_renderer_client.h',
      'atom/renderer/guest_view_container.cc',
      'atom/renderer/guest_view_container.h',
      'atom/utility/atom_content_utility_client.cc',
      'atom/utility/atom_content_utility_client.h',
      'chromium_src/chrome/browser/browser_process.cc',
      'chromium_src/chrome/browser/browser_process.h',
      'chromium_src/chrome/browser/chrome_notification_types.h',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener.cc',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener.h',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener_mac.mm',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener_mac.h',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener_x11.cc',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener_x11.h',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener_win.cc',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener_win.h',
      'chromium_src/chrome/browser/printing/print_job.cc',
      'chromium_src/chrome/browser/printing/print_job.h',
      'chromium_src/chrome/browser/printing/print_job_manager.cc',
      'chromium_src/chrome/browser/printing/print_job_manager.h',
      'chromium_src/chrome/browser/printing/print_job_worker.cc',
      'chromium_src/chrome/browser/printing/print_job_worker.h',
      'chromium_src/chrome/browser/printing/print_job_worker_owner.cc',
      'chromium_src/chrome/browser/printing/print_job_worker_owner.h',
      'chromium_src/chrome/browser/printing/print_view_manager_base.cc',
      'chromium_src/chrome/browser/printing/print_view_manager_base.h',
      'chromium_src/chrome/browser/printing/print_view_manager_basic.cc',
      'chromium_src/chrome/browser/printing/print_view_manager_basic.h',
      'chromium_src/chrome/browser/printing/print_view_manager_observer.h',
      'chromium_src/chrome/browser/printing/printer_query.cc',
      'chromium_src/chrome/browser/printing/printer_query.h',
      'chromium_src/chrome/browser/printing/printing_message_filter.cc',
      'chromium_src/chrome/browser/printing/printing_message_filter.h',
      'chromium_src/chrome/browser/renderer_host/pepper/chrome_browser_pepper_host_factory.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/chrome_browser_pepper_host_factory.h',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_broker_message_filter.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_broker_message_filter.h',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_flash_browser_host.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_flash_browser_host.h',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_flash_clipboard_message_filter.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_flash_clipboard_message_filter.h',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_isolated_file_system_message_filter.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_isolated_file_system_message_filter.h',
      'chromium_src/chrome/browser/speech/tts_controller.h',
      'chromium_src/chrome/browser/speech/tts_controller_impl.cc',
      'chromium_src/chrome/browser/speech/tts_controller_impl.h',
      'chromium_src/chrome/browser/speech/tts_linux.cc',
      'chromium_src/chrome/browser/speech/tts_mac.mm',
      'chromium_src/chrome/browser/speech/tts_message_filter.cc',
      'chromium_src/chrome/browser/speech/tts_message_filter.h',
      'chromium_src/chrome/browser/speech/tts_platform.cc',
      'chromium_src/chrome/browser/speech/tts_platform.h',
      'chromium_src/chrome/browser/speech/tts_win.cc',
      'chromium_src/chrome/browser/ui/browser_dialogs.h',
      'chromium_src/chrome/browser/ui/cocoa/color_chooser_mac.mm',
      'chromium_src/chrome/browser/ui/views/color_chooser_aura.cc',
      'chromium_src/chrome/browser/ui/views/color_chooser_aura.h',
      'chromium_src/chrome/browser/ui/views/frame/global_menu_bar_registrar_x11.cc',
      'chromium_src/chrome/browser/ui/views/frame/global_menu_bar_registrar_x11.h',
      'chromium_src/chrome/common/chrome_utility_messages.h',
      'chromium_src/chrome/common/print_messages.cc',
      'chromium_src/chrome/common/print_messages.h',
      'chromium_src/chrome/common/tts_messages.h',
      'chromium_src/chrome/common/tts_utterance_request.cc',
      'chromium_src/chrome/common/tts_utterance_request.h',
      'chromium_src/chrome/renderer/pepper/chrome_renderer_pepper_host_factory.cc',
      'chromium_src/chrome/renderer/pepper/chrome_renderer_pepper_host_factory.h',
      'chromium_src/chrome/renderer/pepper/pepper_flash_font_file_host.cc',
      'chromium_src/chrome/renderer/pepper/pepper_flash_font_file_host.h',
      'chromium_src/chrome/renderer/pepper/pepper_flash_fullscreen_host.cc',
      'chromium_src/chrome/renderer/pepper/pepper_flash_fullscreen_host.h',
      'chromium_src/chrome/renderer/pepper/pepper_flash_menu_host.cc',
      'chromium_src/chrome/renderer/pepper/pepper_flash_menu_host.h',
      'chromium_src/chrome/renderer/pepper/pepper_flash_renderer_host.cc',
      'chromium_src/chrome/renderer/pepper/pepper_flash_renderer_host.h',
      'chromium_src/chrome/renderer/pepper/pepper_helper.cc',
      'chromium_src/chrome/renderer/pepper/pepper_helper.h',
      'chromium_src/chrome/renderer/pepper/pepper_shared_memory_message_filter.cc',
      'chromium_src/chrome/renderer/pepper/pepper_shared_memory_message_filter.h',
      'chromium_src/chrome/renderer/printing/print_web_view_helper.cc',
      'chromium_src/chrome/renderer/printing/print_web_view_helper_linux.cc',
      'chromium_src/chrome/renderer/printing/print_web_view_helper_mac.mm',
      'chromium_src/chrome/renderer/printing/print_web_view_helper_pdf_win.cc',
      'chromium_src/chrome/renderer/printing/print_web_view_helper.h',
      'chromium_src/chrome/renderer/spellchecker/spellcheck_worditerator.cc',
      'chromium_src/chrome/renderer/spellchecker/spellcheck_worditerator.h',
      'chromium_src/chrome/renderer/tts_dispatcher.cc',
      'chromium_src/chrome/renderer/tts_dispatcher.h',
      'chromium_src/chrome/utility/utility_message_handler.h',
      'chromium_src/library_loaders/libspeechd_loader.cc',
      'chromium_src/library_loaders/libspeechd.h',
      '<@(native_mate_files)',
      '<(SHARED_INTERMEDIATE_DIR)/atom_natives.h',
    ],
    'lib_sources_win': [
      'chromium_src/chrome/browser/ui/views/color_chooser_dialog.cc',
      'chromium_src/chrome/browser/ui/views/color_chooser_dialog.h',
      'chromium_src/chrome/browser/ui/views/color_chooser_win.cc',
      'chromium_src/chrome/browser/printing/pdf_to_emf_converter.cc',
      'chromium_src/chrome/browser/printing/pdf_to_emf_converter.h',
      'chromium_src/chrome/utility/printing_handler.cc',
      'chromium_src/chrome/utility/printing_handler.h',
    ],
    'framework_sources': [
      'atom/app/atom_library_main.h',
      'atom/app/atom_library_main.mm',
    ],
    'locales': [
      'am', 'ar', 'bg', 'bn', 'ca', 'cs', 'da', 'de', 'el', 'en-GB',
      'en-US', 'es-419', 'es', 'et', 'fa', 'fi', 'fil', 'fr', 'gu', 'he',
      'hi', 'hr', 'hu', 'id', 'it', 'ja', 'kn', 'ko', 'lt', 'lv',
      'ml', 'mr', 'ms', 'nb', 'nl', 'pl', 'pt-BR', 'pt-PT', 'ro', 'ru',
      'sk', 'sl', 'sr', 'sv', 'sw', 'ta', 'te', 'th', 'tr', 'uk',
      'vi', 'zh-CN', 'zh-TW',
    ],
    'atom_source_root': '<!(["python", "tools/atom_source_root.py"])',
    'conditions': [
      ['OS=="win"', {
        'app_sources': [
          'atom/browser/resources/win/resource.h',
          'atom/browser/resources/win/atom.ico',
          'atom/browser/resources/win/atom.rc',
          '<(libchromiumcontent_src_dir)/content/app/startup_helper_win.cc',
        ],
      }],  # OS=="win"
    ],
  },
}
