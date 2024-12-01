use std::fs::File;
use std::io::{self, BufRead};



fn main() -> io::Result<()>{
    let reader = io::BufReader::new(
        File::open("input.txt")?
    );
    let mut result = 0u32;
    for line in reader.lines(){
        let line = line?;
        let mut first_numeric: char  = 'a';
        let mut last_numeric: char = 'a';
        for c in line.chars(){
            if c.is_digit(10) {
                if first_numeric == 'a' {
                    first_numeric = c;
                }
                last_numeric = c;
            }
        }
        let mut concatenated: String = String::from(first_numeric);
        concatenated.push(last_numeric);
        result += concatenated.parse::<u32>().unwrap();
    }
    println!("{}", result);
    Ok(())
}