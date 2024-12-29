import logging
from dataclasses import dataclass, field
from typing import Optional

EMPTY = '*'


@dataclass
class Plot:
    x: int
    y: int
    plant: str
    region_neighbours: Optional[list] = field(default_factory=lambda: [])
    neighbours: Optional[list] = field(default_factory=lambda: [])
    region: Optional['Region'] = None

    def __repr__(self):
        return self.plant

@dataclass
class Region:
    plant: str
    plots: Optional[list] = field(default_factory=lambda: [])

    def add_plots(self, plot: Plot):
        if plot not in self.plots:
            self.plots.append(plot)
            plot.region = self
        for neighbour in plot.region_neighbours:
            if neighbour.region is None:
                self.add_plots(neighbour)

    def area(self):
        return len(self.plots)

    def perimeter(self):
        return sum(len(plot.neighbours) for plot in self.plots)

    def outer_perimeter(self):
        per = set()
        for plot in self.plots:
            for neighbour in plot.neighbours:
                per.add((neighbour.x, neighbour.y))
        return per

    def __repr__(self):
        return f"Region({self.plant},{self.area()},{self.perimeter()})"


def to_input(lines):
    plots = []
    rows = []
    empty_row = [EMPTY * len(lines[0])]
    for y, line in enumerate(empty_row + lines + empty_row):
        row = []
        for x, plant in enumerate(EMPTY + line + EMPTY):
            plot = Plot(x, y, plant)
            row.append(plot)
            plots.append(plot)
            if x > 0:
                left_plot = row[x - 1]
                if plot.plant != EMPTY and left_plot.plant == plot.plant:
                    plot.region_neighbours.append(left_plot)
                    left_plot.region_neighbours.append(plot)
                else:
                    plot.neighbours.append(left_plot)
                    left_plot.neighbours.append(plot)
            if y > 0:
                upper_plot = rows[y-1][x]
                if plot.plant != EMPTY and upper_plot.plant == plot.plant:
                    plot.region_neighbours.append(upper_plot)
                    upper_plot.region_neighbours.append(plot)
                else:
                    plot.neighbours.append(upper_plot)
                    upper_plot.neighbours.append(plot)

        print(row)
        rows.append(row)

    regions = []
    for plot in plots:
        if plot.plant != EMPTY and plot.region is None:
            region = Region(plot.plant)
            region.add_plots(plot)
            regions.append(region)
            print(plot, plot.region_neighbours)
    return plots, regions


def test1():
    lines = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""".split('\n')
    plots, regions = to_input(lines)
    cost = 0
    for region in regions:
        print(region, region.area(), region.perimeter())
        cost += region.area() * region.perimeter()
    print("Part 1", cost, cost == 1930)


def main():
    with open('data/aoc2024_day12.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    plots, regions = to_input(lines)
    cost = 0
    for region in regions:
        print(region, region.area(), region.perimeter())
        cost += region.area() * region.perimeter()
    print("Part 1", cost)   # 1465968


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    logging.basicConfig(level=logging.INFO)
    main()
