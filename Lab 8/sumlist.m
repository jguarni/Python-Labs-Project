function [ sumlist ] = Sumlist( numlist )
% This function will return the total sum
% of all the elements in numlist
    sumlist = 0;
    for i = (0:size(numlist,2))
        sumlist = sumlist + i;
    end
end

