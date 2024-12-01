use std::fs::File;
use std::io::{self, BufRead};
use std::collections::HashMap;

fn main() -> io::Result<()>{
    let search_keys: HashMap<String,char> = HashMap::from([
        ("one".to_string(),'1'),
        ("two".to_string(),'2'),
        ("three".to_string(),'3'),
        ("four".to_string(),'4'),
        ("five".to_string(),'5'),
        ("six".to_string(),'6'),
        ("seven".to_string(),'7'),
        ("eight".to_string(),'8'),
        ("nine".to_string(),'9'),
        ("1".to_string(),'1'),
        ("2".to_string(),'2'),
        ("3".to_string(),'3'),
        ("4".to_string(),'4'),
        ("5".to_string(),'5'),
        ("6".to_string(),'6'),
        ("7".to_string(),'7'),
        ("8".to_string(),'8'),
        ("9".to_string(),'9'),
    ]);

    
    let reader = io::BufReader::new(
        File::open("input.txt")?
    );

    let mut result = 0u32;
    for line in reader.lines(){
        let line = line?;
        let chars: Vec<char> = line.chars().collect();
        let n_chars = chars.len();
        let mut first_numeric: char  = 'a';
        let mut last_numeric: char = 'a';
        for search_begin in 0..n_chars+1 {
            for search_end in search_begin..n_chars+1{
                let substr: String = chars[search_begin..search_end].into_iter().collect();
                if search_keys.contains_key(&substr){
                    let found: char = *search_keys.get(&substr).unwrap();
                    if first_numeric == 'a' {
                        first_numeric = found;
                    }
                    last_numeric = found;
                }
            }
        }
        let mut concatenated: String = String::from(first_numeric);
        concatenated.push(last_numeric);
        result += concatenated.parse::<u32>().unwrap();
    }
    println!("{}", result);
    Ok(())
}