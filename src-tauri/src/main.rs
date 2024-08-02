// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use app::{*};

#[tauri::command]
fn b2o(x: i64) -> i64 {
    bin_to_oct(x)
}

#[tauri::command]
fn b2d(x: i64) -> i64 {
    bin_to_dec(x)
}

#[tauri::command]
fn b2h(x: i64) -> String {
    bin_to_hex(x)
}

#[tauri::command]
fn o2b(x: i64) -> i64 {
    oct_to_bin(x)
}

#[tauri::command]
fn o2d(x: i64) -> i64 {
    oct_to_dec(x)
}

#[tauri::command]
fn o2h(x: i64) -> String {
    oct_to_hex(x)
}

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

#[tauri::command]
fn h2b(x: &str) -> i64 {
    hex_to_bin(x)
}

#[tauri::command]
fn h2o(x: &str) -> i64 {
    hex_to_oct(x)
}

#[tauri::command]
fn h2d(x: &str) -> i64 {
    hex_to_dec(x)
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![d2b, d2o, d2h,
            b2o, b2d, b2h,
            o2b, o2d, o2h,
            h2b, h2o, h2d
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
