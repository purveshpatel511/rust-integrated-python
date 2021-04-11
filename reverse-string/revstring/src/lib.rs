#[macro_use] extern crate cpython;

use cpython::{Python, PyResult};

fn reverse_string_rust(_py: Python, val: &str) -> PyResult<String> {
    let new_val = val.to_string();
    let rev_string = new_val.chars().rev().collect();

    Ok(rev_string)
}

py_module_initializer!(libmyrustlib, initlibmyrustlib, PyInit_revstring, |py, m | {
    m.add(py, "__doc__", "This module is implemented in Rust")?;
    m.add(py, "reverse_string_rust", py_fn!(py, reverse_string_rust(val: &str)))?;
    Ok(())
});
