%% Design a Chebychev-II lowpass filter
%% a)
clc; close all; clear all;
% font_size = 12;

%% For Gnu Octave load package signal
% pkg load signal

wp = 2*pi*5E6;  % 5MHz passband edge
ws = 2*pi*10E6; % 10MHz stopband edge
Rp = 2;         % Define the passband edge at -2dB 
Rs = 60;        % Specify 60dB stopband attenuation
fs = 20e6;
Ts = 1/fs;

% Find the required Chebyshev2 filter order for the given specs
[N, ws_new] = cheb2ord(wp, ws, Rp, Rs, 's'); 

% If analog option is not available, e.g. Gnu Octave
% [N, ws_new] = cheb2ord(wp/(2*pi*fs), ws/(2*pi*fs), Rp, Rs); 

fprintf(['\nThe required filter order is %d.\n'],N);

%% b)
[z, p, k] = cheby2(N,Rs,ws_new,'s');

% If analog option is not available, e.g. Gnu Octave
% [z, p, k] = cheby2(N,Rs,ws_new*(2*pi*fs),'s');

sys = zpk(z, p, k);
f = logspace(5, 9, 3000);
[mag, phase] = bode(sys, 2*pi*f);
db = 20*log10(reshape(mag, 1, length(f))); 
angle = reshape(phase, 1, length(f));

% Unwrap the phase to make the jumps consistent and shift to 0 at w=0
angle = 360*unwrap(2*pi*angle/360)/2/pi; 
angle = angle-angle(1);

% Generate the magnitude plot with annotation, phase, and group delay plots
mindB = -80; 
maxdB = 5;
figure(1)
subplot(2,1,1)
% set(gca, 'fontsize', font_size);
semilogx(f, db, 'linewidth', 2), hold on;
line([min(f) 5E6], [-2 -2], 'LineStyle', ':','LineWidth', 2, 'Color', 'r');
line([5E6 5E6], [mindB -2], 'LineStyle', ':','LineWidth', 2, 'Color', 'r');
line([min(f) 10E6], [0 0], 'LineStyle', ':','LineWidth', 2, 'Color', 'r');
line([10E6 10E6], [0 -60], 'LineStyle', ':','LineWidth', 2, 'Color', 'r');
line([10E6 f(end)], [-60 -60], 'LineStyle', ':','LineWidth', 2, 'Color', 'r');

xlabel('Frequency f/Hz') 
ylabel('Magnitude A/dB') 
axis([min(f) max(f) mindB maxdB]), grid;

subplot(2,1,2)
% set(gca, 'fontsize', font_size); 
semilogx(f, angle, 'linewidth', 2), hold on; 
xlabel('Frequency f/Hz') 
ylabel('Phase phi/deg') 
axis([min(f) max(f) -500 100]), grid;

figure(2)
% set(gca, 'fontsize', font_size);
Tgd = -1E9*diff(2*pi*angle/360)./(2*pi*diff(f));
Tgd( abs(Tgd) > 500) = NaN; % Eliminate discontinuities 
semilogx(f(2:end), Tgd, 'linewidth', 2), hold on; 
xlabel('Frequency f/Hz')
ylabel('Group Delay Tgd/ns') 
axis([min(f) max(f) -50 250]), grid;

%% c)
figure(3)
w_limit = 3E8;
% set(gca, 'fontsize', font_size); 
plot(p,'x','linewidth',2)
hold on
plot(z,'o','linewidth',2);
axis([-w_limit w_limit -w_limit w_limit]), axis square; grid;
xlabel('\sigma'), ylabel('j\omega'), title('Complex s-plane')

% Find the angle of each pole w.r.t. the negative real axis to get Q
phi = acos(-real(p)./abs(p));
Qp = 1./(2*cos(phi));
wp_locations = abs(p);
fprintf(' poles [*1e7] wp [*1e7] Qp\n\n') 
disp([p/1e7 wp_locations/1e7 Qp])

%% d)
% Check the Butterworth filter order required for the same specs.
% [N_butter, wn_butter] = buttord(wp, ws, Rp, Rs, 's');

% If analog option is not available
[N_butter, wn_butter] = buttord(wp/(2*pi*fs), ws/(2*pi*fs), Rp, Rs);

fprintf('\nThe required Butterworth filter order is %d.\n',N_butter);

%% e)
figure(4)
% set(gca, 'fontsize', font_size);
semilogx(f, db, 'linewidth', 2), hold on; 
xlabel('Frequency f/Hz')
ylabel('Magnitude A/dB') 
axis([min(f) max(f) mindB maxdB]),grid;

% From manually tweaking the passband back to 2dB at 5MHz using Rs
% [N_butter, wn_butter] = buttord(2*pi*5e6, 2*pi*10e6, 2, 33.78, 's'); 
% [z_butter, p_butter, k_butter] = butter(N_butter,wn_butter,'s');

% If analog option is not available
[N_butter, wn_butter] = buttord(5e6/fs, 10e6/fs, 2, 33.78); 
[z_butter, p_butter, k_butter] = butter(N_butter,wn_butter*(2*pi*fs),'s'); 

sys_butter = zpk(z_butter, p_butter, k_butter);
[mag_butter, phase_butter] = bode(sys_butter, 2*pi*f);
db_butter = 20*log10(reshape(mag_butter, 1, length(f))); 
semilogx(f, db_butter, 'r', 'linewidth', 2), hold on; 
legend('Cheby2 n=6','Butterworth n=6')
phi_butter = acos(-real(p_butter)./abs(p_butter)); 
Qp_butter = 1./(2*cos(phi_butter)); 
wp_locations_butter = abs(p_butter);
fprintf(' poles [*1e7] wp_butter [*1e7] Qp_butter\n\n') 
disp([p_butter/1e7 wp_locations_butter/1e7 Qp_butter])
