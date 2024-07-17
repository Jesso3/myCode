const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    for (0..100000) |i| {
        try stdout.print("{}\n", .{i});
    }
}
