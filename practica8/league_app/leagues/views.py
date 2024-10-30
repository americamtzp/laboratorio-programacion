from django.shortcuts import render, get_object_or_404, redirect
from .models import League
from .forms import LeagueForm

# Vista para listar ligas
def league_list(request):
    leagues = League.objects.all()
    return render(request, 'leagues/league_template.html', {'leagues': leagues, 'form': None, 'league': None, 'confirm_delete': None})

# Vista para crear una liga
def league_create(request):
    if request.method == 'POST':
        form = LeagueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('league_list')
    else:
        form = LeagueForm()
    return render(request, 'leagues/league_template.html', {'form': form})

# Vista para actualizar una liga existente
def league_update(request, pk):
    league = get_object_or_404(League, pk=pk)
    form = LeagueForm(request.POST or None, instance=league)
    if form.is_valid():
        form.save()
        return redirect('league_list')
    return render(request, 'leagues/league_template.html', {'form': form, 'leagues': League.objects.all(), 'league': league, 'confirm_delete': None})

# Vista para eliminar una liga
def league_delete(request, pk):
    league = get_object_or_404(League, pk=pk)
    if request.method == 'POST':
        league.delete()
        return redirect('league_list')
    return render(request, 'leagues/league_template.html', {'leagues': League.objects.all(), 'form': None, 'league': league, 'confirm_delete': True})
