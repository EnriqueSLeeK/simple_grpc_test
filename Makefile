
plot_and_save:
	@mkdir -p 'graph'
	[[ ! -d 'log' ]] || python plot_graph.py
