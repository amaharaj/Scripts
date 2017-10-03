# Usage example: gnuplot -e "filename='Energy'" -e "data='TIP4P data'" ../plot-pred-true.gnu
# Predicted vs. True plots

set terminal push # save current terminal
set terminal unknown

f(x) = x

plot filename u 1:2 with points lc rgb "#696969" pointtype 7 pointsize 0.5 title data, f(x) lt -1 lw 2 lc '#2F4F4F' title ''

set terminal pop # restore previous terminal

min = (GPVAL_Y_MIN < GPVAL_X_MIN ? GPVAL_Y_MIN : GPVAL_X_MIN) # save minimum x and y values
max = (GPVAL_Y_MAX > GPVAL_X_MAX ? GPVAL_Y_MAX : GPVAL_X_MAX) # save maximum x and y values

set xrange[min:max] # use same range for x and y axes
set yrange[min:max]

set size ratio -1 # plot in square box so that dimensions are not skewed

set key on # turn on legend
set key box
set key bottom right
set grid

set xlabel 'True Energy [eV]'
set ylabel 'Predicted Energy [eV]'

replot
pause -1

