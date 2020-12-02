package main

import(
	"fmt"
	"bufio"
	"os"
	"strconv"
)

var target = 2020

func  main()  {
	part1()
	part2()

}

func part1()  {
	var ids = make(map[int]int)
	file, _ := os.Open("input.csv") 
    scanner := bufio.NewScanner(file) 
    scanner.Split(bufio.ScanLines) 


    for scanner.Scan() {
		line, _ := strconv.Atoi(scanner.Text()) 
		ids[line] = line
		var want = target - line

		if val, boo := ids[want]; boo {
			fmt.Println(val * line)
			break
		}
	} 
		
    file.Close() 
}

func part2()  {
	var ids = make(map[int]int)
	file, _ := os.Open("input.csv") 
    scanner := bufio.NewScanner(file) 
    scanner.Split(bufio.ScanLines) 


    for scanner.Scan() {
		line, _ := strconv.Atoi(scanner.Text()) 
		ids[line] = line
		
		for value := range ids {
			var want = target - line - value

			if val, boo := ids[want]; boo {
				fmt.Println(line * value * val)
				return
			}
		}
	} 
		
    file.Close() 
	
}