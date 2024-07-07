#[allow(dead_code)]
pub fn dec_to_bin(mut x: i64) -> i64 {
    let mut i = 0;
    let mut bin = 0;

    while x > 0 {
        if x % 2 == 1 {
            bin = bin + 10_i64.pow(i)
        }
        i += 1;
        x /= 2;
    }

    bin
}

#[allow(dead_code)]
pub fn dec_to_oct(mut x: i64) -> i64 {
    let mut i = 0;
    let mut oct = 0;

    while x > 0 {
        oct += x % 8 * 10_i64.pow(i);
        i += 1;
        x /= 8;
    }

    oct
}

#[allow(dead_code)]
pub fn dec_to_hex(mut x: i64) -> String {
    let mut hex = String::new();

    if x == 0 {
        "0".to_string()
    } else {
        while x > 0 {
            if x % 16 >= 0 && x % 16 < 10 {
                hex.push_str(&(x % 16).to_string());
            } else if x % 16 == 10 {
                hex.push_str("A");
            } else if x % 16 == 11 {
                hex.push_str("B");
            } else if x % 16 == 12 {
                hex.push_str("C");
            } else if x % 16 == 13 {
                hex.push_str("D");
            } else if x % 16 == 14 {
                hex.push_str("E");
            } else if x % 16 == 15 {
                hex.push_str("F");
            }
            x /= 16;
        }
        hex.chars().rev().collect::<String>()
    }
}

#[allow(dead_code)]
pub fn bin_to_dec(mut x: i64) -> i64 {
    let mut i = 0;
    let mut dec = 0;
    while x > 0 {
        dec += x % 2 * 2_i64.pow(i);
        i += 1;
        x /= 10;
    }

    dec
}

#[allow(dead_code)]
pub fn bin_to_oct(x: i64) -> i64 {
    dec_to_oct(bin_to_dec(x))
}

#[allow(dead_code)]
pub fn bin_to_hex(x: i64) -> String {
    dec_to_hex(bin_to_dec(x))
}

#[allow(dead_code)]
pub fn oct_to_dec(mut x: i64) -> i64 {
    let mut i = 0;
    let mut dec = 0;
    while x > 0 {
        dec += x % 10 * 8_i64.pow(i);
        i += 1;
        x /= 10;
    }

    dec
}

#[allow(dead_code)]
pub fn oct_to_bin(x: i64) -> i64 {
    dec_to_bin(oct_to_dec(x))
}

#[allow(dead_code)]
pub fn oct_to_hex(x: i64) -> String {
    dec_to_hex(oct_to_dec(x))
}

#[allow(dead_code)]
pub fn hex_to_dec(x: &str) -> i64 {
    let ui: Vec<char> = x.chars().rev().collect(); // Collect into a Vec<char>
    let mut dec = 0;
    for (i, &c) in ui.iter().enumerate() {
        let value = match c {
            '0'..='9' => c as u32 - '0' as u32,
            'A'..='F' => c as u32 - 'A' as u32 + 10,
            _ => continue, // Skip invalid characters
        };
        dec += value as i64 * 16i64.pow(i as u32);
    }
    dec
}

#[allow(dead_code)]
pub fn hex_to_bin(x: &str) -> i64 {
    dec_to_bin(hex_to_dec(x))
}

#[allow(dead_code)]
pub fn hex_to_oct(x: &str) -> i64 {
    dec_to_oct(hex_to_dec(x))
}
