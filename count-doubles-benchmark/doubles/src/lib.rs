#[macro_use] extern crate cpython;

use cpython::{Python, PyResult};

fn countdoubles(_py: Python, val: &str) -> PyResult<u64> {
    let mut total = 0u64;

    for (c1, c2) in val.chars().zip(val.chars().skip(1)) {
        if c1 == c2 {
            total += 1;
        }
    }

    Ok(total)
}

py_module_initializer!(libmyrustlib, initlibmyrustlib, PyInit_doubles, |py, m | {
    m.add(py, "__doc__", "This module is implemented in Rust")?;
    m.add(py, "countdoubles", py_fn!(py, countdoubles(val: &str)))?;
    Ok(())
});
