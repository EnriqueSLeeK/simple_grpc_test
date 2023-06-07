
plot_and_save:
	@mkdir -p 'graph'
	[[ ! -d 'graph' ]] || python plot_graph.py
