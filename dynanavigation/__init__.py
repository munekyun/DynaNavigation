from fman import DirectoryPaneCommand

class OpenIfDirectoryForRightArrowKey(DirectoryPaneCommand):
  def __call__(self):
    # Detect which pane
    panes = self.pane.window.get_panes()
    this_pane = panes.index(self.pane) # 0 for left pane 1 for right pane

    # If left pane and press -> key, go opposite pane
    if this_pane == 0:
      self.pane.run_command('switch_panes', args = {})

    # If right pane and press -> key, go upper directory
    if this_pane == 1:
      self.pane.run_command('go_up', args = {})

class OpenIfDirectoryForLeftArrowKey(DirectoryPaneCommand):
  def __call__(self):
    # Detect which pane
    panes = self.pane.window.get_panes()
    this_pane = panes.index(self.pane) # 0 for left pane 1 for right pane

    # If right pane and press <- key, go upper directory
    if this_pane == 0:
      self.pane.run_command('go_up', args = {})

    # If left pane and press <- key, go opposite pane
    if this_pane == 1:
      self.pane.run_command('switch_panes', args = {})

