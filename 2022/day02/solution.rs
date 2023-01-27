use std::{fs};

fn parse_data(data: &String) -> Vec<Vec<&str>> {
    let split = data.lines();

    let mut games = Vec::new();
    for game in split {
        let g = game.split_whitespace().collect::<Vec<&str>>();
        
        games.push(g);
    }

    return games;
}

fn part1(data: &[Vec<&str>]) -> i32 {
    let mut total: i32 = 0;

    const RES: [&str; 3] = ["X", "Y", "Z"];
    const PLAYS: [&str; 9] = ["AX", "BY", "CZ", "AY", "BZ", "CX", "AY", "BZ", "CX"];

    for game in data.iter() {
        let a = *game.first().unwrap();
        let b = *game.last().unwrap();

        total += 1 + RES.iter().position(|&s| s == b).unwrap() as i32;
        total += 3 * PLAYS.iter().filter(|&&s| *s.to_string() == format!("{}{}", a, b)).count() as i32;
    }
    
    total
}

fn part2(data: &[Vec<&str>]) -> i32 {
    let mut total: i32 = 0;

    for game in data.iter() {
        let a = *game.first().unwrap();
        let b = *game.last().unwrap();

        if b == "X" {
            total += 1 + ["B","C","A"].iter().position(|&s| s == a).unwrap() as i32;
        } else if b == "Y" {
            total += 4 + ["A","B","C"].iter().position(|&s| s == a).unwrap() as i32;
        } else if b == "Z" {
            total += 7 + ["C","A","B"].iter().position(|&s| s == a).unwrap() as i32;
        }
    }

    total
}

fn main() {
    let dummy: String = fs::read_to_string("data/2022/day02/dummy.txt")
        .expect("Shouldn't happen");
    let dummy_data = parse_data(&dummy);
    let real: String = fs::read_to_string("data/2022/day02/data.txt")
        .expect("Shouldn't happen");
    let real_data = parse_data(&real);

    println!("Part One:\nDummy Data: {}\nReal Data: {}\n", part1(&dummy_data), part1(&real_data));
    // println!("Part One:\nDummy Data: {}", part1(&dummy_data));


    println!("Part Two:\nDummy Data: {}\nReal Data: {}", part2(&dummy_data), part2(&real_data));
    // println!("Part Two:\nDummy Data: {}", part2(&dummy_data));

}