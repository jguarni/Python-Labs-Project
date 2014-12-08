classdef Person
% A person is a human that has a name, date of birth, gender and SSN.
	properties
		Name
		DOB
		Gender
		ssn
    end
	methods
		function obj = Person(Name,DOB,Gender,ssn);
            % Name -- string ex. 'Joe'
            % DOB - String ex. '03/12/1993'
            % Gender - String ex. 'Male'
            % SSN - Integer ex. 123456789
            
			obj.Name = Name;
			obj.DOB = DOB;
			obj.Gender = Gender;
			obj.ssn = ssn;
        end
        
        %fucntion e = afunction(aPerson)
        %   e = Person.Name

        function a = checkAge(obj);
           % This function will check the Persons Age.
           % return -- integer
           
           x = {obj.DOB};
           for i = 1:size(x,2);
               d = char(x(i));
           end
           age = 2013 - str2num(d(7:end))
        end       
    end
end