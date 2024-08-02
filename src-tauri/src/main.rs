// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use app::{dec_to_bin, dec_to_oct, dec_to_hex};

#[tauri::command]
fn d2b(x: i64) -> i64 {
    dec_to_bin(x)
}

#[tauri::command]
fn d2o(x: i64) -> i64 {
    dec_to_oct(x)
}

#[tauri::command]
fn d2h(x: i64) -> String {
    dec_to_hex(x)
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![d2b, d2o, d2h])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
