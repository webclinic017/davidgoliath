def main():
    pass


def best_fit_slope_and_intercept():
    pass


def squared_error(ys_orig, ys_line):
    return sum((ys_line-ys_orig)**2)


def coefficient_of_determination(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return (1 - squared_error_regr/squared_error_y_mean)


if __name__ == "__main__":
    main()
    pass
