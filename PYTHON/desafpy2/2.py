if (getY() > 50) {
    heading(225);
} else if (noWorm()) {
    heading(315);
} else if (getX() > 20) {
    heading(180);
}