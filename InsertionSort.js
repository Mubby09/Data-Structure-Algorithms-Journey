// Insertion Sort is really great for arrays that you are sure are already sorted or close to sorted.
// Insertion Sort is a step more complex but a bit more useful than bubble sort and is occasionally useful.
// The worst case scenerio to is is similar to bubble sort's but its best case make it suited for times when you are sure a listed or likely to be sorted.
// The idea is that the beginning of yoyr list/array is sorted and that everything else is assumed to be unsorted
// An example of that is this:
// const arr =n [10,4,2,6,3,8,1,9];
// Here in the example above, it is assumed that index 0 which is 10 is already sorted and you the only assumed that the remaining elements starting from index 1 which is 4 is unsorted.
// The outer loop goes over the whole list, the index of which signifies where the 'sorted' part of the list is.
// The inner loop goes over the sorted part of the list and inserts it into the correct position in the array.

function insertionSort(arr) {
  for (let i = 1; i < arr.length; i++) {
    for (let j = 0; j < i; j++) {
      if (arr[i] < arr[j]) {
        const insert = arr.splice(i, 1);
        arr.splice(j, 0, insert[0]);
      }
    }
  }
  return arr;
}
console.log(insertionSort([65, 89, 87, 2, 4, 0, 78, 36, 13, 22]));
