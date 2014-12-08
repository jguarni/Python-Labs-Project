function [ sum ] = totalsum( endnum )
% This function will take a parameter
% and return the sum from 0 to the input
% parameter

    sum = 0;
    for i = (0:endnum)
        sum = sum + i;
    end
end

