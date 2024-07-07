// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use app::dec_to_bin;

#[tauri::command]
fn d2b(x: i64) -> i64 {
    dec_to_bin(x)
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![d2b])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
