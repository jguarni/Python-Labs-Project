function [temperatureC] = Convert( temperatureF )
% This function will convert a input temperature
% from farhenheit and returns it in Celsius
% Deduct 32, then multiply by 5, then divide by 9
temperatureC = (((temperatureF - 32) * 5)/9);

end

