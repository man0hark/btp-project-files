numfiles=60000;
for k = 1:numfiles
    m = sprintf('full_label/%d.txt', k);
    n = sprintf('full_csv_label/%d.csv',k);
    YourData = load(m);
    csvwrite(n, YourData);
    clc
    clear
end
