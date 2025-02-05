/**
 * Advent of Code Day 01 Part 01, Version 1
 * 
 * Link to Site: https://adventofcode.com/2024/day/1
 * 
 * Description:
 * Given a file path, this function will:
 * - Read the file contents.
 * - Parse the file to create two lists of numbers (left and right).
 * - Sort both lists.
 * - Validate that the lists are of equal length.
 * - Compute the sum of the absolute differences between corresponding numbers.
 *
 * Returns:
 *   The total distance (summed absolute differences) between the two lists.
 *
 * Throws:
 *   Errors related to file access, parsing, or invalid input.
 */
export function adventOfCodeDay1Part1V1(filePath: string): number {
    try {
      // TODO: Read the file content (e.g., using fs.readFileSync or fs.promises.readFile).
      // const data = <read file data from filePath>;
  
      // TODO: Split the file content by newline characters.
      // const lines = data.split('\n');
  
      // TODO: Parse each line into two numbers.
      // For example:
      //   const left: number[] = lines.map(line => parseInt(line.split(' ')[0]));
      //   const right: number[] = lines.map(line => parseInt(line.split(' ')[1]));
  
      // TODO: Sort both the left and right lists.
      // left.sort((a, b) => a - b);
      // right.sort((a, b) => a - b);
  
      // TODO: Validate that both lists have the same length.
      // if (left.length !== right.length) {
      //   throw new Error("Both lists must have the same number of elements.");
      // }
  
      // TODO: Compute and return the summated distance.
      // return left.reduce((acc, num, i) => acc + Math.abs(num - right[i]), 0);
  
      return 0; // Placeholder return value
    } catch (error) {
      // TODO: Handle specific errors (e.g., file not found, parsing errors).
      throw error;
    }
  }
  
  /**
   * Advent of Code Day 01 Part 01, Version 2
   * 
   * This version:
   * - Reads the file line by line.
   * - Trims each line and filters out any empty ones.
   * - Splits each non-empty line into exactly two number strings.
   * - Converts the strings to numbers with error handling.
   * - Sorts the two resulting lists and computes the total distance.
   *
   * Returns:
   *   The sum of absolute differences between corresponding elements of the sorted lists.
   *
   * Throws:
   *   Errors for file access issues, invalid formatting, or conversion failures.
   */
  export function adventOfCodeDay1Part1V2(filePath: string): number {
    try {
      // TODO: Read the file content line by line.
      // For example, using fs.readFileSync and splitting by newlines:
      // const data = <read file data from filePath>;
      // const lines = data.split('\n').map(line => line.trim()).filter(line => line !== '');
  
      // Initialize empty arrays for left and right numbers.
      // const left: number[] = [];
      // const right: number[] = [];
  
      // TODO: Process each line:
      // for (const line of lines) {
      //   const parts = line.split(/\s+/);
      //   if (parts.length !== 2) {
      //     throw new Error(`Line does not contain exactly two values: '${line}'`);
      //   }
      //   // Attempt to parse both parts to integers.
      //   const leftVal = parseInt(parts[0]);
      //   const rightVal = parseInt(parts[1]);
      //   if (isNaN(leftVal) || isNaN(rightVal)) {
      //     throw new Error(`Could not convert values to int in line: '${line}'`);
      //   }
      //   left.push(leftVal);
      //   right.push(rightVal);
      // }
  
      // TODO: Sort both arrays.
      // left.sort((a, b) => a - b);
      // right.sort((a, b) => a - b);
  
      // TODO: Compute and return the sum of absolute differences.
      // return left.reduce((acc, num, i) => acc + Math.abs(num - right[i]), 0);
  
      return 0; // Placeholder return value
    } catch (error) {
      // TODO: Handle and re-throw errors with additional context if needed.
      throw error;
    }
  }
  
  // -------------------------
  // Execution of the functions
  // -------------------------
  
  // Define file paths (update these paths as needed)
  const realFilePath: string = "./data/day01-pt01-input-real.txt.txt";
  const dummyFilePath: string = "./data/day01-pt01-input-dummy.txt.txt";
  
  // Call the functions. (The actual implementations will compute and return the real answers.)
  const resV1: number = adventOfCodeDay1Part1V1(realFilePath);
  const resV2: number = adventOfCodeDay1Part1V2(realFilePath);
  
  // Log the results (placeholders for now)
  console.log("resV1:", resV1);
  console.log("resV2:", resV2);