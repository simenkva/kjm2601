
#include <math.h>
#include <stdlib.h>

const double pi = 3.141592653589793;

static double laguerrel(const double n, const double k, const double x)
{
    int i;
    double L0, L1 = 0.0;
    double LaguerreL = 1.0;
    for (i = 0; i < n; i++)
    {
        L0 = L1;
        L1 = LaguerreL;
        LaguerreL = ((2 * i + 1 + k - x) * L1 - (i + k) * L0) / (i + 1);
    }
    return LaguerreL;
}


static double Rnl(const int n, const int l, const double r)
{
    // radial wave function
    int i;
    double rho, a;
    rho = 2.0 * r / n;
    a = 4.0;
    for (i = n - l; i <= n + l; i++)
    {
        a /= i;
    }
    a = sqrt(a);
    a /= n * n;
    
    return a * exp(-0.5 * rho) * pow(rho, l) * laguerrel(n-l-1, 2*l+1, rho);
}


static double legendrepn(const int l, int m, const double x)
{
    // renormalized associated legendre polynomials
    // = polar angle part of spherical harmonics
    int i, j;
    double fac, fac1, pn, a, b, c;
    m = abs(m);
    a = 1.0;
    if (m > 0)
    {
        fac = 1.0;
        c = (1.0 + x) * (1.0 - x);
        for (i = 1; i <= m; i++)
        {
            a *= c * fac / (fac + 1.0);
            fac += 2.0;
        }
    }
    a = sqrt((2 * m + 1) * a / (4.0 * pi));
    if (m & 1)
        a = -a;
    if (l == m)
        return a;
    else
    {
        b = a * x * sqrt(2.0 * m + 3.0);
        if (l == m + 1)
            return b;
        else
        {
            fac1 = sqrt(2.0 * m + 3.0);
            for (j = m + 2; j <= l; j++)
            {
                fac = sqrt((4.0 * j * j - 1.0) / (j * j - m * m));
                pn = fac * (b * x - a / fac1);
                fac1 = fac;
                a = b;
                b = pn;
            }
            return pn;
        }
    }
}


void Psi(const int n, const int l, const int m,
    const double x, const double y, const double z,
    double *pabs, double *pphase)
{
    double r, rxy, p0;
    // absolute value of Psi without phi dependency
    r = sqrt(x * x + y * y + z * z);
    if (r == 0.0)
        *pabs = Rnl(n, l, r) * legendrepn(l, m, 0.0);
    else
        *pabs = Rnl(n, l, r) * legendrepn(l, m, z / r);
    
    // phase of Psi
    p0 = (n + l + m + 1) * pi;
    if (*pabs < 0.0)
    {
        *pabs = -*pabs;
        p0 += pi;
    }
    if (m != 0)
    {
        rxy = sqrt(x * x + y * y);
        if (rxy != 0.0)
            p0 += m * atan2(y, x);
    }
    *pphase = fmod(p0, 2.0 * pi);
}


double Psi_sqr(const int n, const int l, const int m,
    const double x, const double y, const double z)
{
    // Probability density function
    double pabs;
    double r = sqrt(x * x + y * y + z * z);
    if (r == 0.0)
        pabs = Rnl(n, l, r) * legendrepn(l, m, 0.0);
    else
        pabs = Rnl(n, l, r) * legendrepn(l, m, z / r);
    return pabs * pabs;
}
