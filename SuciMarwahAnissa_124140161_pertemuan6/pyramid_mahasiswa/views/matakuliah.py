from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPBadRequest
from ..models import Matakuliah


@view_config(route_name='matakuliah_list', renderer='json')
def matakuliah_list(request):
    dbsession = request.dbsession
    matakuliahs = dbsession.query(Matakuliah).order_by(Matakuliah.id.asc()).all()
    return {'matakuliahs': [m.to_dict() for m in matakuliahs]}


@view_config(route_name='matakuliah_detail', renderer='json')
def matakuliah_detail(request):
    dbsession = request.dbsession
    matakuliah_id = request.matchdict['id']
    matakuliah = dbsession.query(Matakuliah).filter_by(id=matakuliah_id).first()
    if matakuliah is None:
        return HTTPNotFound(json_body={'error': f'Matakuliah dengan ID {matakuliah_id} tidak ditemukan'})
    return {'matakuliah': matakuliah.to_dict()}


@view_config(route_name='matakuliah_add', request_method='POST', renderer='json')
def matakuliah_add(request):
    try:
        json_data = request.json_body
        required_fields = ['kode_mk', 'nama_mk', 'sks', 'semester']
        for field in required_fields:
            if field not in json_data or json_data[field] in (None, ''):
                return HTTPBadRequest(json_body={'error': f'Field {field} wajib diisi!'})

        sks = json_data['sks']
        semester = json_data['semester']
        if not isinstance(sks, int) or isinstance(sks, bool) or sks <= 0:
            return HTTPBadRequest(json_body={'error': 'Field sks harus berupa angka bulat lebih dari 0!'})
        if not isinstance(semester, int) or isinstance(semester, bool) or semester <= 0:
            return HTTPBadRequest(json_body={'error': 'Field semester harus berupa angka bulat lebih dari 0!'})

        matakuliah = Matakuliah(
            kode_mk=json_data['kode_mk'],
            nama_mk=json_data['nama_mk'],
            sks=sks,
            semester=semester,
        )
        dbsession = request.dbsession
        dbsession.add(matakuliah)
        dbsession.flush()
        return {'success': True, 'matakuliah': matakuliah.to_dict()}
    except Exception as e:
        return HTTPBadRequest(json_body={'error': str(e)})


@view_config(route_name='matakuliah_update', request_method='PUT', renderer='json')
def matakuliah_update(request):
    dbsession = request.dbsession
    matakuliah_id = request.matchdict['id']
    matakuliah = dbsession.query(Matakuliah).filter_by(id=matakuliah_id).first()
    if matakuliah is None:
        return HTTPNotFound(json_body={'error': f'Matakuliah dengan ID {matakuliah_id} tidak ditemukan'})
    try:
        json_data = request.json_body
        if 'kode_mk' in json_data:
            matakuliah.kode_mk = json_data['kode_mk']
        if 'nama_mk' in json_data:
            matakuliah.nama_mk = json_data['nama_mk']
        if 'sks' in json_data:
            sks = json_data['sks']
            if not isinstance(sks, int) or isinstance(sks, bool) or sks <= 0:
                return HTTPBadRequest(json_body={'error': 'Field sks harus berupa angka bulat lebih dari 0!'})
            matakuliah.sks = sks
        if 'semester' in json_data:
            semester = json_data['semester']
            if not isinstance(semester, int) or isinstance(semester, bool) or semester <= 0:
                return HTTPBadRequest(json_body={'error': 'Field semester harus berupa angka bulat lebih dari 0!'})
            matakuliah.semester = semester
        return {'success': True, 'matakuliah': matakuliah.to_dict()}
    except Exception as e:
        return HTTPBadRequest(json_body={'error': str(e)})


@view_config(route_name='matakuliah_delete', request_method='DELETE', renderer='json')
def matakuliah_delete(request):
    dbsession = request.dbsession
    matakuliah_id = request.matchdict['id']
    matakuliah = dbsession.query(Matakuliah).filter_by(id=matakuliah_id).first()
    if matakuliah is None:
        return HTTPNotFound(json_body={'error': f'Matakuliah dengan ID {matakuliah_id} tidak ditemukan'})
    dbsession.delete(matakuliah)
    return {'success': True, 'message': f'Matakuliah dengan ID {matakuliah_id} berhasil dihapus'}