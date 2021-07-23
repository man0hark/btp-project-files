clc
clear
close all
files = dir('*csv') ;
N = length(files) ;
iwant = cell(N,1) ;
for i = 1:N
   num = csvread(files(i).name) ;
   iwant{i} = num ;
   clear num
end
iwant = cell2mat(iwant) ;

 
% Write the table to a CSV file
writematrix(iwant,'cnn_feat.csv');