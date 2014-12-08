function [ number ] = Fib( n )
% This function will recursivley sum to the n number the user inputs of the
% fibbonacci sequence.
number = zeros(n,1);
number(1) = 1;
number(2) = 2;

for z = 3:n
    number(z) = number(z-1) + number(z-2);
end

