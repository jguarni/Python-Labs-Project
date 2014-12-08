function [ square ] = Sumlist( numlist )
% This function will calculate the square
% for each item in the input list
square=[];
    for i = 1:size(numlist,2)
        square(i) = numlist(i)^2;
        
        
    end
end

