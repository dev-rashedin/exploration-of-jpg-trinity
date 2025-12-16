function primeNumber(num) {
  switch (num) {
    case 2:
    case 3:
    case 5:
    case 7:
      console.log(`${num} is a prime number`);
      break;
    default:
      console.log(`${num} is not a prime number`);
  }
}

primeNumber(2);
primeNumber(3);
primeNumber(5);
primeNumber(7);
primeNumber(8);