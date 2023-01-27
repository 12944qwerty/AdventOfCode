use std::fs;

fn parse_data(data: &String) -> Vec<u32> {
    let split = data.split("\n\n");

    let mut elves = Vec::new();
    for elf in split {
        let cals = elf.lines().map(|x| x.parse::<u32>().unwrap()).sum();
        
        elves.push(cals);
    }

    elves.sort();

    return elves;
}

fn part1(data: &Vec<u32>) -> u32 {
    return *data.get(data.len()-1).unwrap();
}

fn part2(data: &Vec<u32>) -> u32 {
    return data.get(data.len()-4..data.len()-1).unwrap().iter().sum::<u32>();
}

fn main() {
    let dummy: String = fs::read_to_string("data/2022/day01/dummy.txt")
        .expect("Shouldn't happen");
    let dummy_data = parse_data(&dummy);
    let real: String = fs::read_to_string("data/2022/day01/data.txt")
        .expect("Shouldn't happen");
    let real_data = parse_data(&real);

    println!("Part One:\nDummy Data: {}\nReal Data: {}\n", part1(&dummy_data), part1(&real_data));

    println!("Part Two:\nDummy Data: {}\nReal Data: {}", part2(&dummy_data), part2(&real_data));
}