#!/usr/bin/python
# coding: utf-8
from __future__ import print_function

import Xlib.display

display = Xlib.display.Display()

def atom_i2s(integer):
  return display.get_atom_name(integer)

def atom_s2i(string):
  i = display.get_atom(string, only_if_exists=True)
  if i == Xlib.X.NONE:
    raise ValueError('No Atom interned with that name.')
  else:
    return i

def get_property(window, name):
  # length field in X11 is 4 bytes, max it out!
  property = window.get_property(atom_s2i(name), 0, 0, pow(2,32)-1)
  if property is None:
    raise ValueError('Window has no property with that name.')
  # bytes_after != 0 if we fetched it too short
  assert property._data['bytes_after'] == 0
  property_type = atom_i2s(property._data['property_type'])
  if property_type == 'STRING':
    # strings should be served byte-wise
    assert property.format == 8;
    # string arrays are separated by \x00; some have one at the end as well
    values = property.value.split('\x00')
    return values
  else:
    raise NotImplementedError('I’m sorry, I can handle only STRINGs so far.')

if __name__ == '__main__':
  import sys, pipes
  root_window = display.screen().root
  property_name = sys.argv[1]
  print(property_name, end=' ')
  values = [pipes.quote(value) for value in
              get_property(root_window, property_name)]
  print(' '.join(values))
